#! /usr/bin/python
#
__author__ = "thanh"

from rest_framework.response import Response
from core.views.mixins import GenericViewMixin
from rest_framework import status
from core.serializers.room_booking import RoomBookingSerializer
from core.services.room_booking import RoomBookingService


class RoomBookingViewSet(GenericViewMixin):
    permission_classes = ()
    view_set = "room_booking"
    serializer_class = RoomBookingSerializer

    def list(self, request, *args, **kwargs):
        room_booking = RoomBookingService.get_all_room_booking()
        data = {
            'room_booking': self.get_serializer(room_booking, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

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

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            room_booking = RoomBookingService.get(pk=pk)
            if room_booking:
                serializer = self.get_serializer(room_booking)
                data = serializer.data
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        try:
            data = request.data.copy()
            room_booking = RoomBookingService.get(pk=pk)
            serializer = self.get_serializer(room_booking, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            room_booking = RoomBookingService.get(pk=pk)
            if room_booking:
                RoomBookingService.delete(room_booking)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)


