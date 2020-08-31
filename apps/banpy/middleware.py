from django.http import HttpResponseForbidden
from .exceptions import RateLimitException
from .settings import BAN_IPBASED
class RateLimitMiddleware(object):
    """
    Handles exceptions thrown by limited login attepmts.
    """
    def process_exception(self, request, exception):
        if isinstance(exception, RateLimitException):
            if BAN_IPBASED:
                #BAN IP with banpy. set the ip-address to banpy' socket
                return HttpResponseForbidden(
                    'Too many failed login attempts. Try again later. Your ip is banned for a while',
                    content_type='text/plain',
                )

            else:
                return HttpResponseForbidden(
                    'Too many failed login attempts. Try again later.',
                    content_type='text/plain',
                )
#some template???
