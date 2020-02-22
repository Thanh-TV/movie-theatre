#! /usr/bin/python

__author__ = "thanh"

from django.db import models
from core.models.timestamped import TimeStampedModel
from core.managers.ticket import TicketManager


class Ticket(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    seat_number = models.PositiveIntegerField(default=0, db_index=True)
    customer_id = models.PositiveIntegerField(default=0)
    customer_name = models.CharField(max_length=100, default='')
    room_booking_id = models.PositiveIntegerField(default=0, db_index=True)

    objects = TicketManager()

    class Meta:
        db_table = 'ai_tickets'

