from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User, UserProfile

class RegistrationForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username',  'email', 'first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number', 'password')

    def save(self, commit=True):
        #Save the Provided Password in hashed format
        user = super().save(comit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserCreationForm(forms.Form):
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ('username',  'email', 'first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number', 'is_staff', 'is_superuser')

    def clean_password_2(self):
    # Check that the two passwords match
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Passwords Dont Match')
        return password_2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model= User
        fields = ('username',  'email', 'first_name', 'second_name', 'surname', 'date_of_birth', 'phone_number', 'password', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # This is done here  instead of on the db field because the field doesn't have access to the initial Value
        return self.initial['password']



