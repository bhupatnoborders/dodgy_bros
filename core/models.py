from django.db import models

# Create your models here.

USER_TYPES = (
    ('seller', 'Seller'),
    ('buyer', 'Buyer'),
)

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

