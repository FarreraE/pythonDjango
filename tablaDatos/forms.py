from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=10)


class LinkForm(forms.Form):
    facebook = forms.CharField(max_length=50)
    instagram = forms.CharField(max_length=50)
    twiter = forms.CharField(max_length=50)
    whatsApp = forms.CharField(max_length=50)
