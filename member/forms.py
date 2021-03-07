from django import forms
from .models import Member

class JoinForm(forms.ModelForm):

    class Meta:
        model = Member
        fields =['uid', 'upw', 'email', 'phone']

class LoginForm(forms.ModelForm):

    class Meta:
        model = Member
        fields =['uid', 'upw']