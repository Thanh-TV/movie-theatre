#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Customer


class CustomerService:

    @classmethod
    def get_all_customers(cls):
        return Customer.objects.get_all_customers()

    @classmethod
    def get(cls, pk):
        try:
            return Customer.objects.get(pk=pk)
        except:
            return None

    @classmethod
    def save(cls, data, instance=None):
        try:
            customer = instance if instance else Customer()
            for key, value in data.items():
                setattr(customer, key, value)
            customer.save()
            return customer
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