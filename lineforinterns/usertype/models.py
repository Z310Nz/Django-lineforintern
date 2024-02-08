from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        COMPANY = "COMPANY", "Company"
        ADMIN = "ADMIN", "Admin"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


# Student-----------------------------------------------------------------
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STUDENT)


class Student(CustomUser):

    base_role = CustomUser.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Student"


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == CustomUser.Role.STUDENT:
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField


# Student----------------------------------------------------------------


# Company----------------------------------------------------------------


class CompanyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.COMPANY)


class Company(CustomUser):

    base_role = CustomUser.Role.COMPANY

    company = CompanyManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Company"


@receiver(post_save, sender=Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created and instance.role == CustomUser.Role.COMPANY:
        CompanyProfile.objects.create(user=instance)


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name_eng = models.CharField(max_length=100, unique=True, primary_key=True)
    company_name_thai = models.CharField(max_length=100)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=15)
    company_address = models.TextField()
    company_website = models.URLField()
    company_logo = models.ImageField(upload_to="company_logo/")
    company_description = models.TextField()
    company_established = models.DateField


# Company----------------------------------------------------------------
