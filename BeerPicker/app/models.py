"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Beer(models.Model):
    """Beers in the database"""
    beerName = models.CharField(max_length = 200, default = "Beer Name")
    ibu = models.DecimalField(max_digits = 4, decimal_places = 1, default = -1.0)
    abv = models.DecimalField(max_digits = 4, decimal_places = 2, default = -1.0)
    color = models.IntegerField(default = -1)
    location = models.CharField(max_length = 200, default = "Location")

    def __str__(self):
        return self.beerName

class User(models.Model):
    """Registered users"""
    userName = models.CharField(max_length = 200, default = "User name")
    liked_beers = models.ManyToManyField(Beer)
    """disliked_beers = models.ManyToManyField(Beer)
    saved_beers = models.ManyToManyField(Beer)"""

    def __str__(self):
        return self.userName
