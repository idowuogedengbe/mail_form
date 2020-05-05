from django.db import models


# Create your models here.


class Application(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    email = models.EmailField()
    department_select = models.CharField(max_length=100)
    pno = models.CharField(max_length=8)
    phone_no = models.CharField(max_length=11)
    designation = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=False)
    date_applied = models.DateTimeField(auto_now_add=True, )
    date_last_edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.last_name


class Department(models.Model):
    department_hod_title = models.CharField(max_length=20, verbose_name="Title")
    department_hod_last_name = models.CharField(max_length=100, verbose_name="Surname")
    department_hod_first_name = models.CharField(max_length=100, verbose_name="First Name")
    department_hod_other_name = models.CharField(max_length=100, verbose_name="Other Name", null=True)
    department_hod_email = models.EmailField(verbose_name="Email")
    department_name = models.CharField(max_length=100, verbose_name="Name of Department")

    def __str__(self):
        return self.department_name
