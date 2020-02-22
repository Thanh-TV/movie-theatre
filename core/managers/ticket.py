#! /usr/bin/python
#

from django.db.models import Manager, Model

__author__ = "thanh"


# TODO: Implement all methods filter Tickets here
class TicketManager(Manager):

    def get_all_tickets(self, room_booking_id=0):
        if room_booking_id:
            return self.filter(room_booking_id=room_booking_id)
        return self.all()

    def is_ticket_available(self, room_booking_id, seat_number, customer_id=0):
        filter_params = dict(
            room_booking_id=room_booking_id,
            seat_number=seat_number
        )
        exclude_params = {}
        if customer_id:
            exclude_params['customer_id'] = customer_id
        return not self.filter(**filter_params).exclude(**exclude_params).exists()
