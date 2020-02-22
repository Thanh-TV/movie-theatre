#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Movie


class MovieService:

    @classmethod
    def get_all_movies(cls):
        return Movie.objects.get_all_movies()

    @classmethod
    def get(cls, pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            return None

    @classmethod
    def save(cls, data, instance=None):
        try:
            movie = instance if instance else Movie()
            for key, value in data.items():
                setattr(movie, key, value)
            movie.save()
            return movie
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