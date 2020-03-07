from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm

from .models import CustomUser


class CustomUserForm(RegistrationForm):
    birthdate= forms.DateField(widget=forms.TextInput(attrs={
        'class':'datepicker'
    }))

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        widgets = {
            'birthdate': forms.DateInput(attrs={'class':'datepicker'})
        }
        fields = ('username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'nickname', 'picture', 
                'position', 'birthdate')


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')