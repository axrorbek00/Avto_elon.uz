from django.db import models


class CarsModel(models.Model):
    name = models.CharField(max_length=45)
    prise = models.CharField(max_length=255)
    position = models.CharField(max_length=7, null=True)
