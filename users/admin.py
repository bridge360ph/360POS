from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext as _

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username', 'first_name', 'last_name',
        'position'
    ]
    UserAdmin.fieldsets=(
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'nickname', 'birthdate', 'position', 'gas_station_assigned')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)


admin.site.register(CustomUser, CustomUserAdmin)
