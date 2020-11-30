# Generated by Django 3.1 on 2020-11-30 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=32)),
                ('number', models.IntegerField()),
                ('url', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/images')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('last_paid', models.DateField()),
                ('phone_number', models.IntegerField(null=True)),
                ('why_GT', models.CharField(max_length=300)),
                ('what_fav', models.TextField()),
                ('best_spot', models.TextField()),
                ('any_interesting', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='profiles')),
                ('rate', models.FloatField()),
                ('rating', models.FloatField(null=True)),
                ('calendly', models.TextField()),
                ('classes', models.ManyToManyField(blank=True, related_name='tutors', to='home.Class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
