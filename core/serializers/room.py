#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Room
from rest_framework import serializers
from core.services.room import RoomService


class RoomSerializer(serializers.ModelSerializer):
    seats = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Room

    def create(self, validated_data):
        return RoomService.save(validated_data)

    def update(self, instance, validated_data):
        return RoomService.save(validated_data, instance)