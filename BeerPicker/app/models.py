"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    """Location of breweries"""
    location = models.CharField(max_length = 200, default = "Location")

    def __str__(self):
        return self.location

class Brewery(models.Model):
    """Breweries for all beers in database"""
    breweryName = models.CharField(max_length = 200, default = "Brewery")
    location = models.ForeignKey(Location, on_delete = models.CASCADE)

    def __str__(self):
        return self.breweryName

class Beer(models.Model):
    """Beers in the database"""
    beerName = models.CharField(max_length = 200, default = "Beer Name")
    brewery = models.ForeignKey(Brewery, on_delete = models.CASCADE)
    ibu = models.DecimalField(max_digits = 4, decimal_places = 1, default = -1.0)
    abv = models.DecimalField(max_digits = 4, decimal_places = 2, default = -1.0)
    color = models.IntegerField(default = -1)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)

    def __str__(self):
        return self.beerName

class User_Profile(models.Model):
    """Registered users"""
    user = models.OneToOneField(User)
    userName = models.CharField(max_length = 200, default = "User name")
    liked_beers = models.ManyToManyField(Beer)
    """
    disliked_beers = models.ManyToManyField(Beer)
    saved_beers = models.ManyToManyField(Beer)
    """

    def __str__(self):
        return self.userName
