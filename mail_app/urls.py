
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.application, name='application'),
    path('application_list', views.application_list, name='application_list'),
     path('application', views.application, name='application'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
]




