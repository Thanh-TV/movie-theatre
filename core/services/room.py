#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Room


class RoomService:

    @classmethod
    def get_all_rooms(cls):
        return Room.objects.get_all_rooms()

    @classmethod
    def get(cls, pk):
        try:
            return Room.objects.get(pk=pk)
        except:
            return None

    @classmethod
    def save(cls, data, instance=None):
        try:
            room = instance if instance else Room()
            for key, value in data.items():
                setattr(room, key, value)
            room.save()
            return room
        except Exception as ex:
            # todo: handle log
            raise ex

    @classmethod
    def delete(cls, instance):
        try:
            instance.delete()
        except Exception as ex:
            # todo: handle log
            raise ex