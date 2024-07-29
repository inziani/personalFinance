from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username,  email, first_name, second_name, surname,date_of_birth, phone, **extra_fields):
        values = [username, email, first_name, second_name, surname, date_of_birth, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():

            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            username = username,  
            email = email, 
            first_name=first_name, 
            second_name=second_name, 
            surname=surname, 
            date_of_birth=date_of_birth,
            phone=phone, 
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username,  email, first_name, second_name, surname, date_of_birth, phone, Password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username,  email, first_name, second_name, surname, date_of_birth, phone, Password=None, **extra_fields)
    
    def create_superuser(self, username,  email, first_name, second_name, surname, phone, Password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must is_superuser = True.')
        return self._create_user(username,  email, first_name, second_name, surname, date_of_birth, phone, Password=None, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','second_name', 'surname' ,'date_of_birth' ,'phone']

    def get_full_name(self):
        return self.first_name, self.second_name, self.surname

    def get_short_name(self):
        # return self.first_name.split()[0]
        return f'{self.surname}_{self.first_name}'