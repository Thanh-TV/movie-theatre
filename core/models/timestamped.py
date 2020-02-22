from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    # Use this model when you want to handle the timestamp common fields by your-self
    # Actually, should use AutoTimeStampedModel for these common fields
    # and use other fields for handle your business logic
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True