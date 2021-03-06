# Generated by Django 2.2.12 on 2020-04-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('other_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department_select', models.CharField(max_length=100)),
                ('pno', models.CharField(max_length=8)),
                ('phone_no', models.CharField(max_length=11)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('date_last_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_hod_title', models.CharField(max_length=20, verbose_name='Title')),
                ('department_hod_last_name', models.CharField(max_length=100, verbose_name='Surname')),
                ('department_hod_first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('department_hod_other_name', models.CharField(max_length=100, null=True, verbose_name='Other Name')),
                ('department_hod_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('department_name', models.CharField(max_length=100, verbose_name='Name of Department')),
            ],
        ),
    ]
