from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.auth.models import User, Group, Permission


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        COMPANY = "COMPANY", "Company"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.role == self.Role.STUDENT or self.role == self.Role.COMPANY:
                self.is_staff = False
                self.is_superuser = False
            else:
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


class StudentInfo(models.Model):
    profile = models.ImageField(upload_to="profile/", null=True, blank=True)
    student_id = models.IntegerField(
        unique=True, primary_key=True, null=False, blank=False
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    line_id = models.CharField(max_length=200)
    # website = models.URLField()
    cv = models.URLField()
    last_job = models.CharField(max_length=200)
    intern_des = models.CharField(max_length=200)
    intern_company = models.CharField(max_length=200)
    interest_job = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    faculty = models.CharField(max_length=50, blank=True)
    major = models.CharField(max_length=50, blank=True)
    # gpa = models.CharField(max_length=10)
    intern_start = models.DateField()
    intern_end = models.DateField()
    eng_skill = models.CharField(max_length=200)

    def __str__(self):
        return (
            self.first_name
            + " "
            + self.last_name
            + " "
            + str(self.student_id)
            + " "
            + self.email
            + " "
            + self.phone
            + " "
            + self.university
            + " "
            + self.faculty
            + " "
            + self.major
            + " "
            + self.gpa
            + " "
            + str(self.intern_start)
            + " "
            + str(self.intern_end)
            + " "
            + self.eng_skill
            + " "
            + self.interest_job
            + " "
            + self.skill
            + " "
            + self.intern_company
            + " "
            + self.intern_des
            + " "
            + self.last_job
            + " "
            + self.cv
            + " "
            + self.website
            + " "
            + self.line_id
        )


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


class CompanyInfo(models.Model):
    company_name_eng = models.CharField(max_length=100, unique=True, primary_key=True)
    company_name_thai = models.CharField(max_length=100)
    logoc = models.ImageField(upload_to="logos/", null=True, blank=True)
    foundation_date = models.DateField()
    company_type = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    website = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    address_label = models.CharField(max_length=255)
    line_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return (
            self.company_name_eng
            + " "
            + self.company_name_thai
            + " "
            + str(self.foundation_date)
            + " "
            + str(self.number_of_employees)
            + " "
            + self.website
            + " "
            + self.email
            + " "
            + self.address
            + " "
            + self.city
            + " "
            + self.country
            + " "
            + self.province
            + " "
            + self.postal_code
            + " "
            + self.address_label
            + " "
            + self.line_id
        )


class Job(models.Model):
    company = models.ForeignKey(
        CompanyInfo, on_delete=models.CASCADE, null=True, blank=True, default=""
    )
    workplace = models.CharField(max_length=255)
    worktype = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    benefit = models.CharField(max_length=255)
    workstart = models.TimeField()
    workend = models.TimeField()
    workday = models.CharField(max_length=255)


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    companyinfo = models.ForeignKey(
        CompanyInfo, on_delete=models.CASCADE, null=True, blank=True
    )


# Company----------------------------------------------------------------
