# Generated by Django 5.0 on 2024-03-05 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usertype", "0017_alter_studentinfo_intern_end_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="companyinfo",
            old_name="logoc",
            new_name="profile",
        ),
    ]