from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from .models import Onepage,Services,Social,Portfolio,Contact,News,SiteNotice,DataPolicy
from django.shortcuts import render
from django.conf import settings

from django.views.decorators.cache import cache_page

def OnepageIndex(request):

    services=Services.objects.all()
    social=Social.objects.all()
    onepage=Onepage.objects.all()
    contacts=Contact.objects.all()
    news=News.objects.all()[:3]
    if onepage:
        onepage=onepage[0]
    portfolio=Portfolio.objects.all()

    return render(request,
            'onepage/onepage.html',
            {'services': services,
             'socials': social,
             'onepage': onepage,
             'portfolio': portfolio,
             'contacts': contacts,
             'news': news,
            })

def SiteNoticeView(request):
    site_notice=SiteNotice.objects.all()
    if site_notice:
        site_notice=site_notice[0]
    return render(request,
            'onepage/site_notice.html',
            {'site_notice': site_notice,})


def DataPolicyView(request):
    data_policy=DataPolicy.objects.all()[:1]
    if data_policy:
        data_policy=data_policy[0]
    return render(request,
            'onepage/data_policy.html',
            {'data_policy': data_policy,})
