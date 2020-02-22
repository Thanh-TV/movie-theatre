#! /usr/bin/python
#

__author__ = "thanh"

from django.db import transaction
from core.models import Ticket, Customer
from core.services.customer import CustomerService


class TicketService:

    @classmethod
    def get_all_tickets(cls, room_booking_id=0):
        return Ticket.objects.get_all_tickets(room_booking_id=room_booking_id)

    @classmethod
    def is_ticket_available(cls, room_booking_id, seat_number, customer_id=0):
        return Ticket.objects.is_ticket_available(room_booking_id, seat_number, customer_id=customer_id)

    @classmethod
    def get(cls, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except:
            return None

    @classmethod
    def save(cls, data, instance=None):
        try:
            customer_name = data.get('customer_name', '')
            ticket = instance if instance else Ticket()
            with transaction.atomic():
                for key, value in data.items():
                    setattr(ticket, key, value)
                if customer_name:
                    if ticket.customer_id:
                        customer = CustomerService.get(ticket.customer_id)
                    else:
                        customer = Customer()
                    customer.name = customer_name
                    customer.save()
                    ticket.customer_id = customer.id
                ticket.save()
                return ticket
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