from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get', views.parse, name = 'get_parse'),
]