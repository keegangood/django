from django.db import models
from toppings.models import Topping

class Pizza(models.Model):
    name = models.CharField(
        max_length=100,
        required=True,
        unique=True
    )

    toppings = models.ManyToManyField(
        Topping,
        related_name="toppings"
    )

    def __str__(self):
        return self.name
    