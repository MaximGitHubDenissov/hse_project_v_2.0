from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext_lazy as _
import re

class LoginForm(forms.Form):
    username = forms.CharField(
        label=_("Login"),
        error_messages={
            'required': _('Please enter your login.')
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label=_("Password"),
        error_messages={
            'required': _('Please enter your password.')
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Enter')))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Аутентификация пользователя по логину и паролю
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(_("Invalid login or password."))
        return cleaned_data

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label=_('First name'),
        max_length=30,
        error_messages={
            'required': _('Please enter your name.'),
            'max_length': _('The name cannot be longer than 30 characters.')
        }
    )
    last_name = forms.CharField(
        label=_('Last name'),
        max_length=30,
        error_messages={
            'required': _('Please enter your last name.'),
            'max_length': _('The last name cannot be longer than 30 characters.')
        }
    )
    email = forms.EmailField(
        label=_('Email'),
        error_messages={
            'required': _('Please enter your email.'),
            'invalid': _('Please enter a valid email address.')
        }
    )
    username = forms.CharField(
        label=_('Username'),
        max_length=30,
        error_messages={
            'required': _('Please enter your login.')
        }
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        error_messages={
            'required': _('Please enter your password.')
        }
    )
    confirm_password = forms.CharField(
        label= _('Confirm your password'),
        widget=forms.PasswordInput,
        error_messages={
            'required': _('Please confirm your password.')
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Register')))
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(_('Login is already taken. Please choose another.'))
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Проверка длины пароля
        if len(password) < 8:
            raise ValidationError(_('The password must be at least 8 characters.'))

        # Проверка наличия букв, цифр и специальных символов
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError(_('The password must contain at least one letter.'))
        if not re.search(r'[0-9]', password):
            raise ValidationError(_('The password must contain at least one number.'))
        if not re.search(r'[@$!%*?&#]', password):
            raise ValidationError(_('The password must contain at least one special character (@, $, !, %, *, ?, & or #).'))

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError({
                'confirm_password': _('The passwords do not match.')
            })
        return cleaned_data