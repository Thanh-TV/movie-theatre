#! /usr/bin/python
#
__author__ = "thanh"

from rest_framework.response import Response
from core.views.mixins import GenericViewMixin
from rest_framework import status
from core.serializers.movie import MovieSerializer
from core.services.movie import MovieService


class MovieViewSet(GenericViewMixin):
    permission_classes = ()
    view_set = "movie"
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = MovieService.get_all_movies()
        data = {
            'movies': self.get_serializer(movies, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            movie = MovieService.get(pk=pk)
            if movie:
                serializer = self.get_serializer(movie)
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
            movie = MovieService.get(pk=pk)
            serializer = self.get_serializer(movie, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            movie = MovieService.get(pk=pk)
            if movie:
                MovieService.delete(movie)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            # todo: handle log
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)


