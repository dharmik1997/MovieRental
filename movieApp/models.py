from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20)
    avail = models.BooleanField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    city = models.CharField(max_length=25)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + str(self.city)
