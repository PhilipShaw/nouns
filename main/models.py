from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


class Noun(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=True)
    item_type = models.CharField(max_length=50, null=True)
    rating_guess = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    create_for = models.ForeignKey(User, default=1, related_name='recipient')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', null=True)
    #Seen on recipient's end:
    rating = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    #True if noun is unrated, False if noun has been previously rated:
    virgin = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=1000, blank= True)

    def __str__(self):
        return self.user.username

class Rapport(models.Model):
    user = models.OneToOneField(User)
    rapport_score = models.IntegerField(default=0, blank=True, null=True)
    medals = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class NounScore(models.Model):
    rating_score = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    user = models.OneToOneField(Noun, default=0)

    def __int__(self):
        return self.rating_score

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

def link_rapport(sender, **kwargs):
    if kwargs['created']:
        user_rapport = Rapport.objects.create(user=kwargs['instance'])


# def create_noun(sender, **kwargs):
#     if kwargs['created']:
#         func_score = NounScore.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
post_save.connect(link_rapport, sender=User)
#post_save.connect(create_noun, sender=Noun)