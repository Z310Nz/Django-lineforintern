# Generated by Django 5.0 on 2024-01-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastjob',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='lastjob',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='website',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
