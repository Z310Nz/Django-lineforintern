# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    def is_student(self):
        return self.role == 'student'
    def is_company(self):
        return self.role == 'company'
    def __str__(self):
        return self.username
    
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'