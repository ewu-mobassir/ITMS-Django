from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required")

    class Meta:
        model = User
        fields = ('email', 'phone', 'name', 'password1', 'password2', 'user_district')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError("Email is already in use")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            user = User.objects.get(phone=phone)
        except Exception as e:
            return phone
        raise forms.ValidationError("Phone number is already in use")

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            user = User.objects.get(name=name)
        except Exception as e:
            return name
        raise forms.ValidationError("Unknown Error")


class UserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Inavlid email or password")