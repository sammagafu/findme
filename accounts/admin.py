from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
User = get_user_model()
admin.site.unregister(Group)

class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email','firstname', 'lastname','phone_number']
    list_filter = ['is_superuser','is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname','lastname','phone_number')}),
        ('Details', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email','phone_number']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)