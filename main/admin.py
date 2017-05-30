from django.contrib import admin
from main.models import UserProfile
from main.models import Noun, NounScore, Rapport

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Noun)
admin.site.register(NounScore)
admin.site.register(Rapport)
admin.site.site_header = 'Nouns'