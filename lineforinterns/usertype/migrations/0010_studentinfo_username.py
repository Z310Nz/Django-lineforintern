# Generated by Django 5.0 on 2024-02-13 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usertype", "0009_studentinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentinfo",
            name="username",
            field=models.OneToOneField(
                default=78,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]