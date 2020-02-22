#
# Copyright (C) 2017 paradox.ai
#
# Release: 1.0
# @link olivia.paradox.ai
#

import json
import logging

from django.db import connections

logger = logging.getLogger("project")


class BaseService:

    @staticmethod
    def last_query():
        print(connections['default'].queries)

    @classmethod
    def log_exception(cls, exc, full_trace=True):
        try:
            logger.error(exc, exc_info=True, stack_info=full_trace)
        except:
            logger.error("Exception: {0}", str(exc))

    @classmethod
    def log_info(cls, message):
        logger.info(message)

    @classmethod
    def log_debug(cls, message):
        logger.debug(message)

    @classmethod
    def log(cls, message):
        if isinstance(message, Exception):
            cls.log_exception(message)
        else:
            log = message
            try:
                log = json.dumps(message, indent=4)
            except:
                if hasattr(message, "__dict__"):
                    log = message.__dict__
            logger.error(log)

    class Meta:
        abstract = True
