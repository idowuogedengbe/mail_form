from django.shortcuts import render
from .models import Application

# Create your views here.


def application_list(request):
    get_all_applicants = Application.objects.all().order_by("-date_applied")
    return render(request, 'mail_app/application_list.html', {"get_all_applicants" : get_all_applicants})