from django import forms
from .models import User

class JoinForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['username', 'password', 'name', 'email', 'phone']

# class LoginForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields =['username', 'password']