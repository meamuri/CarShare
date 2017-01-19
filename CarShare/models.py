from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)


class Driver(models.Model):
    """
    Водитель. Может быть владельцем нескольких машин
    Хранит информацию о всех поездках, в том чилсе прошедших
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Car(models.Model):
    """
    Машина. Информация о водителе. Связь по внешнему ключу с владельцем
    """
    owner = models.ForeignKey(Driver)
    model = models.CharField(max_length=255)


class Passenger(Profile):
    """
    Пассажир. Информация о путешествиях, в том числе и прошедших
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Trip(models.Model):
    """
    Поездка. Откуда, куда, время отбытия и время в пути
    """
    driver = models.ForeignKey(Driver)
    passenger = models.ForeignKey(Passenger)
    city_from = models.CharField(max_length=128)
    city_to = models.CharField(max_length=128)
    when_start = models.DateTimeField()
    road_time = models.DateTimeField()
