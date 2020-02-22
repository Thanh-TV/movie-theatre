#! /usr/bin/python
#

__author__ = "thanh"

from core.models import Customer
from rest_framework import serializers
from core.services.customer import CustomerService


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer

    def create(self, validated_data):
        return CustomerService.save(validated_data)

    def update(self, instance, validated_data):
        return CustomerService.save(validated_data, instance)