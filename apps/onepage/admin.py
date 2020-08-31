from django.contrib import admin
from .models import *
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
#languages
from hvad.admin import TranslatableAdmin,TranslatableModelForm
from hvad.utils import get_translation_aware_manager
#editor
from ckeditor.widgets import CKEditorWidget

class CKAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class OnepageAdmin(TranslatableAdmin):
    list_display=('__unicode__','create_date')
    fieldsets = [
        (_('Landing Page'),{'fields': ['title','landing_subtitle','image']}),
        (_('Intro'),{'fields': ['intro_title','intro_description','intro_image']}),
        (_('Callout'),{'fields': ['callout_title','callout_image']}),
        (_('Map'),{'fields': ['map_title','map_src','map_link']}),
    ]
    list_filter = ['create_date','last_update']
    date_hierachy = 'create_date'

class ServicesAdmin(TranslatableAdmin,CKAdmin):
    list_display=('__unicode__','create_date')
    fieldsets = [
        (_('Services'),{'fields': ['title','service_description','display']}),
    ]
    list_filter = ['create_date','last_update']
    date_hierachy = 'create_date'

class PortfolioAdmin(TranslatableAdmin):
    fieldsets = [
        (_('Partner'),{'fields': ['title','image','link']}),
    ]
    list_filter = ['create_date','last_update']
    date_hierachy = 'create_date'
    list_display=('__unicode__','create_date')



class ContactAdmin(TranslatableAdmin):

    list_display=('__unicode__','create_date')
    fieldsets = [
        (_('Contact'),{'fields':['title','country','city','street','plz']}),
        (_('Phonenumbers'),{'fields':['phone']}),
        (_('Mail Adresses'),{'fields':['mail']}),
    ]
    filter_horizontal = ('phone','mail')

    list_filter = ['create_date','last_update']
    date_hierachy = 'create_date'

class MailAdmin(admin.ModelAdmin):
    list_display=('mail','create_date')
    fields = ['mail',]
    search_fields=['mail',]


class PhoneAdmin(admin.ModelAdmin):
    fields = ['name','number','fax',]
    list_display=('name','number','last_update')

class SocialAdmin(TranslatableAdmin):
    list_display=('network','create_date')
    fieldsets = [
        (_('Social'),{'fields': ['title','network','link']}),
    ]
    list_filter = ['create_date','last_update']
    date_hierachy = 'create_date'


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SiteNoticeAdmin(TranslatableAdmin,CKAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    fields = ['title','content']

class DataPolicyAdmin(TranslatableAdmin,CKAdmin):
    fields = ['title','content']

admin.site.register(News, NewsAdmin)
admin.site.register(Mail,MailAdmin)
admin.site.register(Phone,PhoneAdmin)
admin.site.register(Onepage,OnepageAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Social,SocialAdmin)
admin.site.register(SiteNotice,SiteNoticeAdmin)
admin.site.register(DataPolicy,DataPolicyAdmin)
