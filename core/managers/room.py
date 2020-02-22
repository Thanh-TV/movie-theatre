#! /usr/bin/python
#

from django.db.models import Manager

__author__ = "thanh"


# TODO: Implement all methods filter Rooms here
class RoomManager(Manager):

    def get_all_rooms(self):
        return self.all()
