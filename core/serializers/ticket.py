#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Ticket
from rest_framework import serializers
from core.services.ticket import TicketService
from core.services.room_booking import RoomBookingService
from core.services.room import RoomService
from core.services.utils import Utils


class TicketSerializer(serializers.ModelSerializer):
    room_booking_id = serializers.IntegerField(required=True)
    seat_number = serializers.IntegerField(required=True)
    customer_name = serializers.CharField(required=True)

    class Meta:
        model = Ticket

    def create(self, validated_data):
        return TicketService.save(validated_data)

    def update(self, instance, validated_data):
        return TicketService.save(validated_data, instance)

    def validate(self, data):
        room_booking_id = Utils.safe_int(data.get('room_booking_id'), default=0)
        invalid_booking = False
        room_booking = RoomBookingService.get(room_booking_id)
        if not room_booking:
            invalid_booking = True
        if not invalid_booking:
            room = RoomService.get(room_booking.room_id)
            if not room:
                invalid_booking = True
        if invalid_booking:
            raise Exception("The movie plan is cancelled!")
        seat_number = Utils.safe_int(data.get('seat_number'), default=0)
        if not seat_number or seat_number > room.seats:
            raise Exception("The seat number is invalid!")
        customer_id = self.instance.id if self.instance else 0
        if not TicketService.is_ticket_available(room_booking_id, seat_number, customer_id=customer_id):
            raise Exception("The seat number is already booked!")
        return data