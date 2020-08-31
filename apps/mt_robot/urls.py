from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

urlpatterns = patterns(
    'apps.mt_robot.views',
    url(r'^$','get_robots', name='robots_rule_list'),

)
