from django import forms

from .models import (Picture, Profile, Car,)

class ProfileUpdateViewForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birthday", "email", 'img']
        

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['seller']
        
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['img']

from django.forms.models import inlineformset_factory

CarPicturesFormset = inlineformset_factory(Car, Picture,  fields = ['img',], extra=1)
