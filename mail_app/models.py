
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