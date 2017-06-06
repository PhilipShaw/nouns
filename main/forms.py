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
    # name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Write a post...'
    #     }
    # ))
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

class SnatchForm(forms.ModelForm):

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