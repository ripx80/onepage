import logging
import warnings
from datetime import datetime, timedelta
from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache
from .exceptions import RateLimitException
from .settings import *
logger = logging.getLogger('banpy')


class RateLimitMixin(object):
    """
    A mixin to enable rate-limiting in an existing authentication backend.
    """
    cache_prefix = 'banpy_limit'
    minutes = BAN_TIME
    requests = BAN_REQUESTS
    ip_based = BAN_IPBASED

    username_key = 'username'

    def authenticate(self, **kwargs):
        request = kwargs.pop('request', None)
        username = kwargs[self.username_key]
        if request is not None:
            counts = self.get_counters(request)
            if sum(counts.values()) >= self.requests:
                logger.warning(
                    u"Login rate-limit reached: username '{0}', IP {1}".format(
                        username, request.META['REMOTE_ADDR']
                    )
                )
                raise RateLimitException('Login-Limit reached', counts)
        else:
            warnings.warn(u"No request passed to the backend, unable to "
                          u"rate-limit. Username was '%s'" % username,
                          stacklevel=2)
        user = super(RateLimitMixin, self).authenticate(**kwargs)
        if user is None and request is not None:
            logger.info(
                u"Login failed: username '{0}', IP {1}".format(
                    username,
                    request.META['REMOTE_ADDR'],
                )
            )
            cache_key = self.get_cache_key(request)
            self.cache_incr(cache_key)
        return user

    def get_counters(self, request):
        return cache.get_many(self.keys_to_check(request))

    def keys_to_check(self, request):
        now = datetime.now()
        return [
            self.key(
                request,
                now - timedelta(minutes=minute),
            ) for minute in range(self.minutes + 1)
        ]

    def get_cache_key(self, request):
        return self.key(request, datetime.now())

    def key(self, request, dt):
        return '%s%s-%s' % (
            self.cache_prefix,
            request.META.get('REMOTE_ADDR', ''),
            dt.strftime('%Y%m%d%H%M'),
        )

    def cache_incr(self, key):
        """
        Non-atomic cache increment operation. Not optimal but
        consistent across different cache backends.
        """
        cache.set(key, cache.get(key, 0) + 1, self.expire_after())

    def expire_after(self):
        """Cache expiry delay"""
        return (self.minutes + 1) * 60


class LimitLogin(RateLimitMixin, ModelBackend):
    pass



