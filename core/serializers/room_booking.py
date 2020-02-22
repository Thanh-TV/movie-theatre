#! /usr/bin/python
#

__author__ = "thanh"

from datetime import timedelta
from core.models import RoomBooking
from rest_framework import serializers
from core.services.room_booking import RoomBookingService
from core.services.utils import Utils
from core.services.movie import MovieService
from core.services.room import RoomService


class RoomBookingSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(required=True)
    movie_id = serializers.IntegerField(required=True)
    booked_at = serializers.CharField(required=True)

    class Meta:
        model = RoomBooking

    def create(self, validated_data):
        return RoomBookingService.save(validated_data)

    def update(self, instance, validated_data):
        return RoomBookingService.save(validated_data, instance)

    def validate(self, data):
        room_id = Utils.safe_int(data.get('room_id', 0))
        movie_id = Utils.safe_int(data.get('movie_id', 0))
        room = RoomService.get(room_id)
        if not room:
            raise Exception("Room is invalid!")
        movie = MovieService.get(movie_id)
        if not movie:
            raise Exception("Movie is invalid!")
        booked_at = data.get('booked_at', '')
        booked_at = Utils.string_to_date(booked_at)
        hour_start, minute_start = Utils.string_to_hour_minute(movie.start_at)
        if hour_start > 0 or minute_start > 0:
            booked_at = booked_at.replace(hour=hour_start, minute=minute_start)
        booked_end_at = booked_at + timedelta(minutes=movie.minutes)
        data['booked_at'] = booked_at
        data['booked_end_at'] = booked_end_at
        if not self.instance:
            existed_booking = RoomBookingService.existed_room_booking(room_id, movie_id, booked_at)
            if existed_booking:
                self.instance = existed_booking
        return data