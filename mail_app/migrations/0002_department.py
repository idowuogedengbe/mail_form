# Generated by Django 2.2.12 on 2020-04-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_hod_title', models.CharField(max_length=20, verbose_name='Title')),
                ('department_hod_last_name', models.CharField(max_length=100, verbose_name='Surname')),
                ('department_hod_first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('department_hod_other_name', models.CharField(max_length=100, verbose_name='Other Name')),
                ('department_hod_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('department_name', models.CharField(max_length=100, verbose_name='Name of Department')),
            ],
        ),
    ]
