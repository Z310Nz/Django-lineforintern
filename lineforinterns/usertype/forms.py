# forms.py
from django import forms
from .models import CustomUser, StudentInfo, CompanyInfo, Job, Interview


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
    company = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

class InterviewForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    location = forms.CharField(max_length=100)
    link = forms.URLField()

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['profile', 'cv', 'first_name', 'last_name', 'nick_name', 'student_id', 'email', 'phone', 'gender', 'birthday', 'last_job', 'intern_company', 'interest_job', 'skill', 'eng_skill', 'university', 'faculty', 'major', 'intern_start', 'intern_end']

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['profile'].required = False
        self.fields['cv'].required = False

class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = ['company_name_eng', 'company_name_thai', 'email', 'phone', 'company_des', 'logoc', 'foundation_date', 'number_of_employees', 'website', 'address', 'sub_district', 'district', 'province', 'country', 'postal_code', 'phone', 'line_id']

    def __init__(self, *args, **kwargs):
        super(EditCompanyForm, self).__init__(*args, **kwargs)
        self.fields['logoc'].required = False