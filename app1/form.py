from django import forms
from .models import JobApplication

class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    cover_letter = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'cover_letter', 'resume']
