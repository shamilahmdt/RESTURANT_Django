from django.db import models

class Category(models.Model):
    # name = models.TextField()
    name = models.CharField(max_length=255)
    dishes = models.IntegerField()
    image = models.ImageField(upload_to='category')

class Menu(models.Model):
    name = models.CharField(max_length=255)
    discrimption = models.TextField()
    image = models.ImageField(upload_to='menu')