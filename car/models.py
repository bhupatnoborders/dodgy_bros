from django.db import models
from core.models import TimeStampModel

# Create your models here.

class Car(TimeStampModel):
    CONDITION_TYPES = (
        ('poor', 'Poor'),
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )
    seller_name = models.CharField(max_length=255)
    seller_mobile = models.CharField(max_length=255)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateTimeField()
    condition = models.CharField(max_length=255, choices=CONDITION_TYPES, 
        default="good", db_index=True)
    price = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seller_name}"