# forms.py
from django import forms
from .models import CustomUser


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
    profile = forms.ImageField()  #
    student_id = forms.IntegerField()  #
    first_name = forms.CharField(max_length=100)  #
    last_name = forms.CharField(max_length=100)  #
    nick_name = forms.CharField(max_length=100)  #
    birthday = forms.DateField()  #
    gender = forms.CharField(max_length=200)  #
    email = forms.EmailField()  #
    phone = forms.CharField(max_length=10)  #
    # line_id = forms.CharField(max_length=200)
    # website = forms.URLField()
    cv = forms.URLField()  #
    last_job = forms.CharField(max_length=200)  #
    # intern_des = forms.CharField(max_length=200)
    intern_company = forms.CharField(max_length=200)  #
    interest_job = forms.CharField(max_length=200)  #
    skill = forms.CharField(max_length=200)  #
    university = forms.CharField(max_length=200)  #
    faculty = forms.CharField(max_length=50)  #
    major = forms.CharField(max_length=50)  #
    # gpa = forms.CharField(max_length=10)
    intern_start = forms.DateField()  #
    intern_end = forms.DateField()  #
    eng_skill = forms.CharField(max_length=200)  #


class SignUpCompanyForm(forms.Form):
    company_name_eng = forms.CharField(max_length=100)  #
    company_name_thai = forms.CharField(max_length=100)  #
    email = forms.EmailField()  #
    phone = forms.CharField(max_length=15)  #
    company_des = forms.CharField()  #
    logoc = forms.ImageField()  #
    foundation_date = forms.DateField()  #
    number_of_employees = forms.IntegerField()  #
    website = forms.URLField()  #
    email = forms.EmailField()  #
    address = forms.CharField(max_length=255)  #
    sub_district = forms.CharField(max_length=255)  #
    district = forms.CharField(max_length=255)  #
    province = forms.CharField(max_length=255)  #
    country = forms.CharField(max_length=255)  #
    postal_code = forms.CharField(max_length=255)  #
    phone = forms.CharField(max_length=15)  #
    line_id = forms.CharField(max_length=255)  #

class PostJobForm(forms.Form):
    jobname = forms.CharField(max_length=100)
    jobdes = forms.CharField()
    worktype = forms.CharField(max_length=100) 
    benefit = forms.CharField(max_length=100)
    workstart = forms.TimeField()
    workend = forms.TimeField()
    workday = forms.CharField(max_length=100)
    requirement = forms.CharField(max_length=100)
    qualifications = forms.CharField(max_length=100)
    skills = forms.CharField(max_length=100)