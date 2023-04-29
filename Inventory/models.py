from django.db import models


class Inventory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField(default=0)
    current_stock = models.FloatField(default=0)