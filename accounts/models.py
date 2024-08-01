from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    # picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','second_name', 'surname' ,'date_of_birth' ,'phone_number']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return f'{self.first_name}, {self.second_name}, {self.surname}'

    def get_short_name(self):
        # return self.first_name.split()[0]
        return f'{self.surname}_{self.first_name}'

    def __str__(self):
        return f'{self.first_name}, {self.second_name}, {self.surname}'

class UserProfile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
  education_bio = models.CharField(max_length=255, blank=True, null=True)
  professional_bio = models.CharField(max_length=255, blank=True, null=True)
  professional_hobbies = models.CharField(max_length=255, blank=True, null=True)
  personal_hobbies = models.CharField(max_length=255, blank=True, null=True)
  social_hobbies = models.CharField(max_length=255, blank=True, null=True)
  profile_pic = models.ImageField(null=True)
  is_verified = models.BooleanField(default=False)
  create_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{ self.user.surname } { self.user.middle_name } { self.user.first_name }'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)