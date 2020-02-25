from django import forms

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
                'nickname', 'picture', 'position', 'birthdate')