# Generated by Django 5.0 on 2024-03-21 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usertype", "0002_remove_companyinfo_country_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="company_id",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jobs",
                to="usertype.companyinfo",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="intern_company",
            field=models.TextField(blank=True, default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="last_job",
            field=models.TextField(blank=True, default=21),
            preserve_default=False,
        ),
    ]
