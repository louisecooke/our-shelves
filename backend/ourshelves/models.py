from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])

    def _str_(self):
        return self.title + ": " + self.author