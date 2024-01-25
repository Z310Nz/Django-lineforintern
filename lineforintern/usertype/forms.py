# forms.py

from django import forms
from django.contrib.auth import authenticate
from .models import Student, Company, Professor

class BaseLineLoginForm(forms.Form):
    line_user_info = None
    user_type = None

    def clean(self):
        cleaned_data = super().clean()
        self.user = authenticate(self.request, line_user_info=self.line_user_info, user_type=self.user_type)
        if not self.user:
            raise forms.ValidationError("Invalid Line login.")
        return cleaned_data

class StudentLoginForm(BaseLineLoginForm):
    user_type = 'student'

class CompanyLoginForm(BaseLineLoginForm):
    user_type = 'company'

class ProfessorLoginForm(BaseLineLoginForm):
    user_type = 'professor'
