#! /usr/bin/python

__author__ = "thanh"

from django.db import models
from core.models.timestamped import TimeStampedModel
from core.models.usertypes import TinyIntegerField
from core.managers.movie import MovieManager


class Movie(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    start_at = models.CharField(max_length=20, default='')
    minutes = TinyIntegerField(default=0)

    objects = MovieManager()

    class Meta:
        db_table = 'ai_movies'

    def __str__(self):
        return self.name
