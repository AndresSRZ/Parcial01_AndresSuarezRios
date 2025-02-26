from django.db import models

# Create your models here.
class Flight(models.Model):
    NATIONAL = 'Nacional'
    INTERNATIONAL = 'Internacional'

    FLIGHT_TYPES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]

    name = models.CharField(max_length=255)
    flight_type = models.CharField(max_length=20, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.flight_type}) - ${self.price}"