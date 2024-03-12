# Generated by Django 5.0 on 2024-03-12 03:33

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name_eng", models.CharField(max_length=100)),
                ("company_name_thai", models.CharField(max_length=100)),
                ("company_des", models.TextField()),
                (
                    "profile",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                ("foundation_date", models.DateField()),
                ("number_of_employees", models.IntegerField()),
                ("website", models.URLField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("sub_district", models.TextField()),
                ("district", models.TextField()),
                ("province", models.TextField()),
                ("country", models.TextField()),
                ("postal_code", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("line_id", models.CharField(blank=True, max_length=255)),
                ("facebook", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Interview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("location", models.CharField(max_length=255)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jobname", models.CharField(max_length=255)),
                ("jobdes", models.TextField()),
                ("worktype", models.CharField(max_length=255)),
                ("quality", models.TextField()),
                ("benefit", models.TextField()),
                ("workstart", models.TimeField()),
                ("workend", models.TimeField()),
                ("workday", models.CharField(max_length=255)),
                ("requirement", models.TextField()),
                ("qualifications", models.TextField(blank=True, null=True)),
                ("skills", models.TextField()),
                ("company", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="StudentInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                ("student_id", models.IntegerField()),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("nick_name", models.CharField(max_length=100)),
                ("birthday", models.DateField(blank=True, null=True)),
                ("gender", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("line_id", models.CharField(max_length=200)),
                ("cv", models.URLField()),
                ("last_job", models.TextField()),
                ("intern_company", models.TextField()),
                ("interest_job", models.TextField()),
                ("skill", models.TextField()),
                ("university", models.CharField(max_length=200)),
                ("faculty", models.TextField(blank=True)),
                ("major", models.TextField(blank=True)),
                ("intern_start", models.DateField(blank=True, null=True)),
                ("intern_end", models.DateField(blank=True, null=True)),
                ("eng_skill", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("STUDENT", "Student"),
                            ("COMPANY", "Company"),
                            ("ADMIN", "Admin"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("FINDING", "Finding"),
                            ("PENDING", "Pending"),
                            ("APPROVED", "Approved"),
                            ("REJECTED", "Rejected"),
                            ("INTERVIEW", "Interview"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "unique_together": {("username",)},
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("usertype.customuser",),
            managers=[
                ("admin", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
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
            name="Student",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("usertype.customuser",),
            managers=[
                ("student", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "companyinfo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usertype.companyinfo",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job",
                    models.ManyToManyField(related_name="companies", to="usertype.job"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Matching",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=255)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usertype.companyinfo",
                    ),
                ),
                (
                    "interview",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usertype.interview",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="usertype.job"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usertype.studentinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "studentinfo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usertype.studentinfo",
                    ),
                ),
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
