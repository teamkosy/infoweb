from django import forms
from .models import User
# from django.contrib.auth.forms import UserChangeForm

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['username', 'password']


class JoinForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['username', 'password', 'last_name', 'first_name', 'email', 'phone']


class UpdateForm(forms.ModelForm):

    class Meta:
        medel = User
        fields = ['password', 'last_name', 'first_name', 'email', 'phone']


