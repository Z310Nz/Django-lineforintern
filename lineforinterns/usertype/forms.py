# forms.py
from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpStudentForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    nick_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)


class SignUpCompanyForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=100)
    company_name_eng = forms.CharField(max_length=100)
    company_address = forms.CharField(max_length=100)
    company_email = forms.EmailField()
    company_phone = forms.CharField(max_length=15)


class RoleSelectionForm(forms.Form):
    role = forms.CharField(max_length=100)
