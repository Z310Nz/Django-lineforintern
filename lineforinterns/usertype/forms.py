# forms.py
from django import forms
from .models import CustomUser, Student, Company
from student.models import StudentInfo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    ROLE_CHOICES = [
        ("", "choose role"),
        (CustomUser.Role.STUDENT, "Student"),
        (CustomUser.Role.COMPANY, "Company"),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)


class SignUpStudentForm(forms.Form):
    profile = forms.ImageField()
    student_id = forms.IntegerField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    nick_name = forms.CharField(max_length=100)
    birthday = forms.DateField()
    gender = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    line_id = forms.CharField(max_length=200)
    website = forms.URLField()
    cv = forms.URLField()
    last_job = forms.CharField(max_length=200)
    intern_des = forms.CharField(max_length=200)
    intern_company = forms.CharField(max_length=200)
    interest_job = forms.CharField(max_length=200)
    skill = forms.CharField(max_length=200)
    university = forms.CharField(max_length=200)
    faculty = forms.CharField(max_length=50)
    major = forms.CharField(max_length=50)
    gpa = forms.CharField(max_length=10)
    intern_start = forms.DateField()
    intern_end = forms.DateField()
    eng_skill = forms.CharField(max_length=200)


class SignUpCompanyForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=100)
    company_name_eng = forms.CharField(max_length=100)
    company_address = forms.CharField(max_length=100)
    company_email = forms.EmailField()
    company_phone = forms.CharField(max_length=15)
