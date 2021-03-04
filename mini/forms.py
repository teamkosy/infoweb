from django import forms
from .models import Message

class MsgForm(forms.ModelForm):

    class Meta:
        model = Message
        fields =['title', 'name', 'contents']