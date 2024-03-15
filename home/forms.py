from django import forms
from .models import madahy1


class madahy(forms.Form):
    daste = forms.CharField(max_length=200)
    title = forms.CharField(max_length=200)
    matn = forms.TextInput()
    file = forms.FileField()

