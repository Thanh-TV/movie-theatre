#! /usr/bin/python
#

from django.db.models import Manager
from datetime import datetime, timedelta
from core.services.utils import Utils

__author__ = "thanh"


# TODO: Implement all methods filter Room Booking here
class RoomBookingManager(Manager):

    def get_all_room_booking(self, room_id=0, incoming_booking=False):
        if incoming_booking:
            yesterday = datetime.now() - timedelta(days=1)
            yesterday_end_date = Utils.end_of_date(yesterday)
            return self.filter(room_id=room_id, booked_at__gt=yesterday_end_date)
        return self.all()

    def existed_room_booking(self, room_id, movie_id, booked_at):
        return self.filter(room_id=room_id, movie_id=movie_id, booked_at=booked_at).first()
