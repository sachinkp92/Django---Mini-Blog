from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class Article(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

