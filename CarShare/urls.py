from django.conf.urls import url
from . import views

app_name = 'car_share'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trips/$', views.trips, name='trips'),
]