from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    likes = models.PositiveIntegerField()


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique = True)
