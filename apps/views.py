from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from django.shortcuts import render_to_response,redirect,get_object_or_404,render,redirect
from django.conf import settings
from .onepage.views import OnepageIndex,SiteNoticeView,DataPolicyView
