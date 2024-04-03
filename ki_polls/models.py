
# Create your models here.
from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
