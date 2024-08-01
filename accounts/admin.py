from django.contrib import admin
from django.contrib.auth import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager

from .models import User, UserProfile
from .forms import UserCreationForm, UserChangeForm

# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_plural_name ="User Profile"
    foreignkey_name = 'user'

class CustomUserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number')
    inline = (UserProfileInline)
    list_filter = ('is_superuser',)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal Info', { 'fields': ('first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number','picture')}),
        ('Groups', { 'fields': ('groups,')}),
        ('Permissions', {'fields': ('user_permissions',)})
    )
    fieldsets = UserAdmin.fieldsets + (
  ('Personal Information', 
  {'fields':(
    'date_of_birth',
    )
    }),
  )
    search_fields = ('email', 'phone_number')
    ordering = ('surname',)
    filter_horizonal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)   
