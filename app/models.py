from django.db import models

class Animals(models.Model):

    owner = models.CharField(max_length=50, null=False, blank=False)
    animalName = models.CharField(max_length=50, null=False, blank=False)
    breed = models.CharField(max_length=50, null=False, blank=False)
    contact = models.CharField(max_length=30, null=False, blank=False)
    updateOn = models.DateTimeField(auto_now_add = True)