from django import forms
from .models import Event
from users.models import Athlete

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'desc', 'date', 'location', 'last_reg_date', 'entry_fee', 'prize', 'contact_no', 'ig_handle', 'fb_handle']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter event title'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Enter event description'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter event date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter event location'}),
            'last_reg_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter last registration date'}),
            'entry_fee': forms.NumberInput(attrs={'placeholder': 'Enter entry fee'}),
            'prize': forms.NumberInput(attrs={'placeholder': 'Enter prize amount'}),
            'contact_no': forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
            'ig_handle': forms.TextInput(attrs={'placeholder': 'Enter Instagram handle'}),
            'fb_handle': forms.TextInput(attrs={'placeholder': 'Enter Facebook handle'})
        }

class EventRegistrationForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    contact_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter your contact number'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}))
    gender = forms.ChoiceField(choices=Athlete.GENDER_CHOICES)
    height = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter your height'}))
    weight = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter your weight'}))
    weight_category = forms.ChoiceField(choices=Athlete.WEIGHT_CATEGORY_CHOICES)
    fighting_style = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your fighting style'}))
    club_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your club name'}))