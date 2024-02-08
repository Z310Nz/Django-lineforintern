# Generated by Django 5.0 on 2024-02-08 18:18

import django.contrib.auth.models
import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usertype", "0002_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("usertype.customuser",),
            managers=[
                ("company", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "company_name_eng",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("company_name_thai", models.CharField(max_length=100)),
                ("company_email", models.EmailField(max_length=254)),
                ("company_phone", models.CharField(max_length=15)),
                ("company_address", models.TextField()),
                ("company_website", models.URLField()),
                ("company_logo", models.ImageField(upload_to="company_logo/")),
                ("company_description", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                (
                    "student_id",
                    models.IntegerField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("nick_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]