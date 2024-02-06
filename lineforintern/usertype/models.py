# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    line_user_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    line_token = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def is_student(self):
        return self.role == 'student'
    def is_company(self):
        return self.role == 'company'
    def __str__(self):
        return self.username
    
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.user.username
class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.user.username