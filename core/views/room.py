#! /usr/bin/python
#
__author__ = "thanh"

from rest_framework.response import Response
from core.views.mixins import GenericViewMixin
from rest_framework import status
from core.serializers.room import RoomSerializer
from core.services.room import RoomService
from core.services.room_booking import RoomBookingService


class RoomViewSet(GenericViewMixin):
    permission_classes = ()
    view_set = "room"
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        rooms = RoomService.get_all_rooms()
        data = {
            'rooms': self.get_serializer(rooms, many=True).data
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
            room = RoomService.get(pk=pk)
            if room:
                serializer = self.get_serializer(room)
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
            room = RoomService.get(pk=pk)
            serializer = self.get_serializer(room, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            room = RoomService.get(pk=pk)
            if room:
                room_in_used = RoomBookingService.room_is_in_used(room.id)
                if room_in_used:
                    return Response({'error': 'Room is already in used'}, status=status.HTTP_400_BAD_REQUEST)
                RoomService.delete(room)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)


