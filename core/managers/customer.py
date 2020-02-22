#! /usr/bin/python
#

from django.db.models import Manager

__author__ = "thanh"


# TODO: Implement all methods filter Customers here
class CustomerManager(Manager):

    def get_all_customers(self):
        return self.all()
