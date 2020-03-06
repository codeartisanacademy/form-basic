from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=200)
    synopsis = models.TextField(blank=True, null=True)
