# Generated by Django 5.0 on 2024-03-01 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usertype", "0007_alter_job_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="city",
        ),
        migrations.RemoveField(
            model_name="job",
            name="company",
        ),
        migrations.RemoveField(
            model_name="job",
            name="country",
        ),
    ]
