from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        COMPANY = "COMPANY", "Company"
        ADMIN = "ADMIN", "Admin"

    base_role = Role.ADMIN

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
    
    class Meta:
        unique_together = ['username']

    class StatusUser(models.TextChoices):
        FINDING = (
            "FINDING",
            "Finding",
        )
        PENDING = (
            "PENDING",
            "Pending",
        )
        APPROVED = (
            "APPROVED",
            "Approved",
        )
        REJECTED = (
            "REJECTED",
            "Rejected",
        )
        INTERVIEW = (
            "INTERVIEW",
            "Interview",
        )

    base_status = StatusUser.FINDING

    status = models.CharField(max_length=50, choices=StatusUser.choices)


# Student-----------------------------------------------------------------
class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STUDENT)


class Student(CustomUser):

    base_role = CustomUser.Role.STUDENT
    base_status = CustomUser.StatusUser.FINDING

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
    phone = models.CharField(max_length=15)
    line_id = models.CharField(max_length=200)
    cv = models.URLField()
    last_job = models.TextField()
    intern_company = models.TextField()
    interest_job = models.TextField()
    skill = models.TextField()
    university = models.CharField(max_length=200)
    faculty = models.TextField(blank=True)
    major = models.TextField(blank=True)
    intern_start = models.DateField(blank=True, null=True)
    intern_end = models.DateField(blank=True, null=True)
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
            + self.last_job
            + " "
            + self.cv
            + " "
            + self.line_id
        )


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


class Job(models.Model):
    jobname = models.CharField(max_length=255)
    jobdes = models.TextField()
    worktype = models.CharField(max_length=255)
    quality = models.TextField()
    benefit = models.TextField()
    workstart = models.TimeField()
    workend = models.TimeField()
    workday = models.CharField(max_length=255)
    requirement = models.TextField()
    qualifications = models.TextField(blank=True, null=True)
    skills = models.TextField()
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return (
            self.jobname
            + " "
            + self.jobdes
            + " "
            + self.worktype
            + " "
            + self.quality
            + " "
            + self.benefit
            + " "
            + str(self.workstart)
            + " "
            + str(self.workend)
            + " "
            + self.workday
            + " "
            + self.requirement
            + " "
            + self.qualifications
            + " "
            + self.skills
            + " "
            + self.company
            + " "
            + self.city
            + " "
            + self.country
        )


class CompanyInfo(models.Model):
    company_name_eng = models.CharField(max_length=100, unique=True, primary_key=True)
    company_name_thai = models.CharField(max_length=100)
    company_des = models.TextField()
    profile = models.ImageField(upload_to="profile/", null=True, blank=True)
    foundation_date = models.DateField()
    number_of_employees = models.IntegerField()
    website = models.URLField()
    email = models.EmailField()
    address = models.TextField()
    sub_district = models.TextField()
    district = models.TextField()
    province = models.TextField()
    country = models.TextField()
    postal_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
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
            + ""
            + self.country
            + " "
            + self.province
            + " "
            + self.postal_code
            + " "
            + self.line_id
            + " "
            + self.company_des
            + ""
            + self.sub_district
            + ""
            + self.district
            + ""
            + self.phone
            + ""
        )


class Interview(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return (
            self.company
            + " "
            + self.student
            + " "
            + str(self.date)
            + " "
            + str(self.time)
            + " "
            + self.location
            + " "
            + self.status
            + " "
            + self.link
        )


# Company----------------------------------------------------------------


# Admin----------------------------------------------------------------
class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.ADMIN)


class Admin(CustomUser):
    base_role = CustomUser.Role.ADMIN
    admin = AdminManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Admin"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.role == self.Role.ADMIN:
                self.is_staff = True
                self.is_superuser = True
        return super().save(*args, **kwargs)


# Admin----------------------------------------------------------------
    

# Profile----------------------------------------------------------------
class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    studentinfo = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    companyinfo = models.ForeignKey(
        CompanyInfo, on_delete=models.CASCADE, null=True, blank=True
    )
    job = models.ManyToManyField(Job, related_name="companies")


# Profile----------------------------------------------------------------


# Matching----------------------------------------------------------------
class Matching(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.student.first_name} - {self.job.jobname} - {self.company.company_name_eng}"
# Matching----------------------------------------------------------------
