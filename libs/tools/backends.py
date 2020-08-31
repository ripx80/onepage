from ratelimitbackend.backends import RateLimitModelBackend

class LimitLogin(RateLimitModelBackend):
    minutes = 1
    requests = 3

    #if you will block only the user not the ip
    #~ def key(self, request, dt):
        #~ return '%s%s-%s-%s' % (
            #~ self.cache_prefix,
            #~ request.META.get('REMOTE_ADDR', ''),
            #~ request.POST['username'],
            #~ dt.strftime('%Y%m%d%H%M'),
        #~ )
