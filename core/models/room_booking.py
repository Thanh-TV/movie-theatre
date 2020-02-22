#! /usr/bin/python

__author__ = "thanh"

from django.db import models
from core.models.timestamped import TimeStampedModel
from core.managers.room_booking import RoomBookingManager


class RoomBooking(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    room_id = models.PositiveIntegerField(default=0, db_index=True)
    movie_id = models.PositiveIntegerField(default=0, db_index=True)
    booked_at = models.DateTimeField(null=True, default=None)
    booked_end_at = models.DateTimeField(null=True, default=None)

    objects = RoomBookingManager()

    class Meta:
        db_table = 'ai_room_booking'

