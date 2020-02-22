#! /usr/bin/python
#

__author__ = "thanh"

from core.models import RoomBooking


class RoomBookingService:

    @classmethod
    def get_all_room_booking(cls):
        return RoomBooking.objects.get_all_room_booking()

    @classmethod
    def room_is_in_used(cls, room_id):
        return RoomBooking.objects.get_all_room_booking(room_id=room_id, incoming_booking=True)

    @classmethod
    def existed_room_booking(cls, room_id, movie_id, booked_at):
        return RoomBooking.objects.existed_room_booking(room_id, movie_id, booked_at)

    @classmethod
    def get(cls, pk):
        try:
            return RoomBooking.objects.get(pk=pk)
        except:
            return None

    @classmethod
    def save(cls, data, instance=None):
        try:
            if instance:
                room_booking = instance
            else:
                room_booking = RoomBooking()
            for key, value in data.items():
                setattr(room_booking, key, value)
            room_booking.save()
            return room_booking
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