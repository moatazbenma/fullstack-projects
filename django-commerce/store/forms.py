from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms




class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']