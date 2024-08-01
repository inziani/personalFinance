from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, 
    username,  
    email,
    password, 
    first_name, 
    second_name, 
    surname,
    date_of_birth, 
    phone_number, 
    **extra_fields):
        if not email:
            raise ValueError('Email is a required Field')
        email = self.normalize_email(email)
        user = self.model(
            username = username,  
            email = email, 
            first_name=first_name, 
            second_name=second_name, 
            surname=surname, 
            date_of_birth=date_of_birth,
            phone_number=phone_number, 
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username,  email, first_name, second_name, surname, date_of_birth, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username,  email, first_name, second_name, surname, date_of_birth, phone_number, **extra_fields)
    
    def create_superuser(self, email, first_name, second_name, surname, phone_number , password, username=None, **extra_fields):
        username=username
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must is_superuser = True.')
        return self._create_user(email, first_name, second_name, surname, date_of_birth, phone_number, password, username=None, **extra_fields)

