from django.conf.urls import url
from . import views

app_name = 'CarShare'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trips/$', views.trips, name='trips'),
    url(r'^add/$', views.add_trip, name='add'),
    url(r'^to_book/([0-9]+)/$', views.to_book, name='to_book'),
]