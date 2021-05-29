from django.contrib.auth import get_user_model
from django import forms



class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Primeiro Nome', required=True)
    last_name = forms.CharField(max_length=30, label='Sobrenome')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()