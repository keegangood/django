from django.db import models

class Topping(models.Model):
    name = models.CharField(
        max_length = 100,
        required   = True,
        unique     = True,
    )

    