# Generated by Django 3.1 on 2020-11-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201123_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
