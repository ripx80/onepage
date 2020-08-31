from django.conf import settings
BAN_TIME = getattr(settings, 'BAN_TIME', 1)
BAN_REQUESTS=getattr(settings, 'BAN_REQUEST', 3)
BAN_IPBASED=getattr(settings, 'BAN_IPBASED', False)
#BAN_USE_IPTABLES=getattr(settings, 'BAN_USE_IPTABLES', False)

