#! /usr/bin/python

__author__ = "thanh"

from django.db import models
from core.models.timestamped import TimeStampedModel
from core.managers.room import RoomManager


class Room(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    seats = models.PositiveIntegerField(default=0)

    objects = RoomManager()

    class Meta:
        db_table = 'ai_rooms'

    def __str__(self):
        return self.name
