from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
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
