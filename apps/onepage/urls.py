from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',)

urlpatterns += patterns('apps.project.views',
    url(r'^site-notice/$', 'ProjectSiteNotice',name='site-notice'),
    url(r'^data-privacy/$','ProjectDataPrivacy',name='data-privacy'),
)

