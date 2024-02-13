from django import forms
from usertype.models import CustomUser
from .models import StudentInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "role"]


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = [
            "profile",
            "student_id",
            "first_name",
            "last_name",
            "nick_name",
            "birthday",
            "gender",
            "email",
            "phone",
            "line_id",
            "website",
            "cv",
            "last_job",
            "intern_des",
            "intern_company",
            "interest_job",
            "skill",
            "gpa",
            "intern_start",
            "intern_end",
            "eng_skill",
            "university",
            "faculty",
            "major",
        ]

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
