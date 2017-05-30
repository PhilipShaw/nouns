from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import Noun, UserProfile, NounScore

class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class MakeNoun(forms.ModelForm):
    class Meta:
        model = Noun
        fields = (
            'name',
            'image_url',
            'description',
            'item_type',
            'rating_guess',
            'create_for',
            #'created_by'
        )

# class ScoreForm(forms.ModelForm): #not being used right now
#     class Meta:
#         model = NounScore
#         fields = (
#             'rating_score',
#             'user',
#         )

class ScoreForm2(forms.ModelForm):
    class Meta:
        model = Noun
        fields = (
            'rating',
        )

class UserProfileEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'description',

        )