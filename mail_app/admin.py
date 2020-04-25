from django.contrib import admin

# Register your models here.
from .models import Application, Department


admin.site.register(Application)
admin.site.register(Department)

