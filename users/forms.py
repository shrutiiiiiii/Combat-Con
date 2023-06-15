from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
  
class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}))
    is_athlete = forms.BooleanField(required=False)
    is_host = forms.BooleanField(required=False)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'is_athlete', 'is_host']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm your password'}),
        }

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if self.data.get('is_athlete') == True:
            MyUser.is_athlete = True
        elif self.data.get('is_host') == True:
            MyUser.is_host = True

        if commit:
            user.save()
        return user
    
class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = ['name', 'profile_picture', 'contact_number', 'date_of_birth', 'age', 'gender', 'height', 'weight', 'weight_category', 'fighting_style', 'club_name', 'coach_name', 'record']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'required': True}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter your contact number', 'required': True}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter your date of birth', 'required': True}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter your age', 'required': True}),
            'gender': forms.Select(attrs={'placeholder': 'Select your gender', 'required': True}),
            'height': forms.NumberInput(attrs={'placeholder': 'Enter your height', 'required': True}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter your weight', 'required': True}),
            'weight_category': forms.Select(attrs={'placeholder': 'Select your weight category'}),
            'fighting_style': forms.TextInput(attrs={'placeholder': 'Select your fighting style', 'required': True}),
            'club_name': forms.TextInput(attrs={'placeholder': 'Enter your club name', 'required': True}),
            'coach_name': forms.TextInput(attrs={'placeholder': 'Enter your coach name', 'required': True}),
            'record': forms.TextInput(attrs={'placeholder': 'Enter your record', 'required': True}),
        }

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['name', 'contact_number', 'organization_name', 'events_hosted']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'required': True}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter your contact number', 'required': True}),
            'organization_name': forms.TextInput(attrs={'placeholder': 'Enter your organization name', 'required': True}),
            'events_hosted': forms.TextInput(attrs={'placeholder': 'Enter the events you have hosted', 'required': True}),
        }