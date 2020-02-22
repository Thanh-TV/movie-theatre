#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Movie
from rest_framework import serializers
from core.services.movie import MovieService
from core.services.utils import Utils


class MovieSerializer(serializers.ModelSerializer):
    minutes = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    start_at = serializers.CharField(required=True)

    class Meta:
        model = Movie

    def create(self, validated_data):
        return MovieService.save(validated_data)

    def update(self, instance, validated_data):
        return MovieService.save(validated_data, instance)

    def validate(self, data):
        start_at = data.get('start_at', '')
        hour_start, minute_start = Utils.string_to_hour_minute(start_at)
        is_valid_hour = 0 <= hour_start <= 23
        is_valid_minute = 0 <= minute_start <= 59
        if hour_start is None or not is_valid_hour or not is_valid_minute:
            raise Exception("Start at is invalid!")
        return data