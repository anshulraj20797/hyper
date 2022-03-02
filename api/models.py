from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.IntegerField()
    checked = models.BooleanField()
    description = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name