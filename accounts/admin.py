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

    readonly_fields = ['date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser']
    list_display = ('email','first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number')
    inlines = (UserProfileInline,)
    list_filter = ('is_superuser',)

    add_fieldsets = UserAdmin.add_fieldsets + (
      ((None, {'fields': ('username', 'email', 'password_1', 'password_2','first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number','is_staff', 'is_active', 'is_superuser', )})),
    )
    fieldsets = UserAdmin.fieldsets + (
      ((None, {'fields': ('email', 'password',)})),
      (('Personal Information', {'fields':('first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number')})),
      (('Permissions'), { 'fields': ('is_active', 'is_staff', 'is_superuser', 'groups','user_permissions')}),
      (('Important Dates'), { 'fields': ('last_login', 'date_joined')}),
  )
    search_fields = ('email', 'phone_number')
    ordering = ('surname',)
    filter_horizonal = ()

    # def has_change_permission(self, request, obj=None):
    #    if not request.user.is_superuser:
    #      if obj:
    #        if isinstance(obj, User):
    #          if obj.is_staff:
    #            return False
    #      else:
    #        return True
    #      return True

    # def has_delete_permission(self, request, obj=None):
    #    if not request.user.is_superuser:
    #     if obj:
    #       if isinstance(obj, User):
    #         if obj.is_staff:
    #           return False
    #    else:
    #      return True
    #    return True

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)   
