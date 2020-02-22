#! /usr/bin/python
#
__author__ = "thanh"

from rest_framework.response import Response
from core.views.mixins import GenericViewMixin
from rest_framework import status
from core.serializers.ticket import TicketSerializer
from core.services.ticket import TicketService
from core.services.utils import Utils


class TicketViewSet(GenericViewMixin):
    permission_classes = ()
    view_set = "ticket"
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        room_booking_id = Utils.safe_int(request.GET.get('room_booking_id', 0))
        tickets = TicketService.get_all_tickets(room_booking_id)
        data = {
            'tickets': self.get_serializer(tickets, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            tiket = TicketService.get(pk=pk)
            if tiket:
                serializer = self.get_serializer(tiket)
                data = serializer.data
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        try:
            data = request.data.copy()
            tiket = TicketService.get(pk=pk)
            serializer = self.get_serializer(tiket, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            tiket = TicketService.get(pk=pk)
            if tiket:
                TicketService.delete(tiket)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)


