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
        fields = ["profile", "student_id", "first_name", "last_name", "nick_name", "birthday",  
              'gender','email', 'phone', 'line_id', 'website', 'cv', 'last_job', 'intern_des',
              'intern_company','interest_job','skill','gpa','intern_start','intern_end',
              'eng_skill','university', 'faculty', 'major']