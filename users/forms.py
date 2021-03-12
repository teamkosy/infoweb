from django import forms
from .models import User

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['username', 'password']


class JoinForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['username', 'password', 'last_name', 'first_name', 'email', 'phone']


