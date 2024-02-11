from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import StudentInfo
from company.models import CompanyInfo


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        COMPANY = "COMPANY", "Company"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.role == self.Role.STUDENT:
                self.is_staff = False
                self.is_superuser = False
            elif self.role == self.Role.COMPANY:
                self.is_staff = False
                self.is_superuser = False
            elif self.role == self.Role.ADMIN:
                self.is_staff = True
                self.is_superuser = True
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
    studentinfo = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)


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
    companyinfo = models.ForeignKey(
        CompanyInfo, on_delete=models.CASCADE, null=True, blank=True
    )


# Company----------------------------------------------------------------
