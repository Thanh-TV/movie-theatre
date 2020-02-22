#! /usr/bin/python

__author__ = "thanh"

from django.db import models
from core.models.timestamped import TimeStampedModel
from core.managers.customer import CustomerManager


class Customer(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    # More fields here, just keep simple for now

    objects = CustomerManager()

    class Meta:
        db_table = 'ai_customers'

    def __str__(self):
        return self.name
