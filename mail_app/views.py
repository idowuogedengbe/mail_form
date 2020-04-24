from django.shortcuts import render

# Create your views here.


def application_list(request):
    return render(request, 'mail_app/application_list.html', {})