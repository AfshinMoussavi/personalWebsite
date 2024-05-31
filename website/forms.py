from django import forms
from .models import Contace

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contace
        fields = '__all__'