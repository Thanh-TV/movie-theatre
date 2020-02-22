#! /usr/bin/python

#
# Copyright (C) 2017 paradox.ai
#
# Release: 1.0
# @link olivia.paradox.ai
#
__author__ = "hien"
__date__ = "$Sep 9, 2015 11:04:25 AM$"

from django.db import models


class TinyIntegerField(models.SmallIntegerField):

    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return "tinyint"
        else:
            return super(TinyIntegerField, self).db_type(connection)

