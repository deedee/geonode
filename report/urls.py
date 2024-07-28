from . import views
from django.conf.urls import url
from django.contrib import admin

app_name = 'report'

urlpatterns = [
    url(r'^$', 
        views.home, name='home'),
    url(r'^buatlaporan/$', 
        views.pelaporan, name='pelaporan'),
    url(r'^admin/login/$', 
        admin.site.login, name='login'),
]
