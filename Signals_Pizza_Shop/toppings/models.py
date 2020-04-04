from django.db import models
from pizzas.models import Pizza

UNITS = [
    ('oz', 'ounce'),
    ('floz', 'fluid ounce'),
    ('pc', 'piece'),
    ('slc', 'slice')
]

class Topping(models.Model):
    name = models.CharField(
        max_length = 100,
        unique = True,
    )

    pizzas = models.ManyToManyField(Pizza)

    quantity = models.DecimalField(max_digits=4, decimal_places=2)

    units = models.CharField(max_length=4, choices=UNITS)

    def __str__(self):
        return f"{self.name} - {self.quantity}{self.units}"