# Generated by Django 5.0 on 2024-02-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentInfo",
            fields=[
                (
                    "profile",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                (
                    "student_id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("nick_name", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
                ("line_id", models.CharField(max_length=200)),
                ("website", models.URLField()),
                ("cv", models.URLField()),
                ("intern_job", models.CharField(max_length=200)),
                ("intern_des", models.CharField(max_length=200)),
                ("intern_company", models.CharField(max_length=200)),
                ("interest_job", models.CharField(max_length=200)),
                ("skill", models.CharField(max_length=200)),
                ("education", models.CharField(max_length=200)),
                ("gpa", models.CharField(max_length=10)),
                ("intern_start", models.DateField()),
                ("intern_end", models.DateField()),
                ("eng_skill", models.CharField(max_length=200)),
            ],
        ),
    ]
