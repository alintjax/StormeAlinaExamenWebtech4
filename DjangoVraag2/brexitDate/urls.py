from django.conf.urls import url
from . import views

app_name = 'brexitDate'

urlpatterns = [
    url(r'^', views.index, name='index'),
]