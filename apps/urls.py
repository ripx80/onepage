from django.conf.urls import patterns, include, url
#uncommend if banpy is not used
#from django.contrib import admin

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from apps import views #project views
from apps.banpy import admin

from django.contrib import sitemaps
#from apps.post.urls import sitemaps as post_sitemap
from apps.sitemaps import StaticViewSitemap

sitemaps={'static': StaticViewSitemap(),}
#sitemaps.update(post_sitemap)

admin.autodiscover()

urlpatterns = patterns('',)
urlpatterns+=patterns('django.contrib.sitemaps.views',
    #(r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap\.xml$', 'sitemap', {'sitemaps': sitemaps}),
    (r'^robots\.txt$', include('apps.mt_robot.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=patterns('',
        (r'^__debug__/', include(debug_toolbar.urls)),
        ('^404/$', TemplateView.as_view(template_name='404.html')),
        ('^500/$', TemplateView.as_view(template_name='500.html')),
    )

urlpatterns += i18n_patterns('',
    url(r'^$', views.OnepageIndex, name='index'),
    url(r'^site-notice/$', views.SiteNoticeView, name='site_notice'),
    url(r'^data-policy/$', views.DataPolicyView, name='data_policy'),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/', include(admin.site.urls)),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


