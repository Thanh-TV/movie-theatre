#! /usr/bin/python
#

from django.db.models import Manager

__author__ = "thanh"


# TODO: Implement all methods filter Movies here
class MovieManager(Manager):

    def get_all_movies(self):
        return self.all()
