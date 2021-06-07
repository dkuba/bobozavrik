from django import forms

from .models import Profile

class ProfileUpdateViewForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birthday", "email", 'img']
