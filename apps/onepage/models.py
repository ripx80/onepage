"""Onepage Project Modules.

.. moduleauthor::  ripx80 <mail>

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from libs.tools.models import ShortenSlug,AutoSlugField
from libs.tools import storage
from django.conf import settings
from django.utils import timezone

from django.utils.timezone import now as datetime_now
#translation
from hvad.models import TranslatableModel, TranslatedFields

class CoreObject(models.Model):
    '''Abstract Core Object'''
   # slug = AutoSlugField(_('slug'),populate_from='title', unique=True, db_index=True,overwrite=True)
    last_update = models.DateField(_('last updated'),db_index=True,auto_now=True)
    create_date = models.DateTimeField(_('created date'), default=timezone.now)

    class Meta:
        abstract=True
        ordering = ["-create_date"]

    def __unicode__(self):
        return u'%s: %s' % (self._meta.verbose_name,self.last_update)

class Intro(TranslatableModel):
    intro_image = models.ImageField(_('Intro'),upload_to = storage.hashed_upload_to('intro_image'),null=True,blank=True)#default = 'images/None/default.jpg'
    translations = TranslatedFields(
        intro_title  = models.CharField(_('Intro Title'),max_length=100, db_index=True),
        intro_description  = models.TextField(_('Intro Description Field'),help_text=_('please insert some description here'),blank=True),
    )

    class Meta:
            verbose_name = _('Intro')
            verbose_name_plural = _('Intro')
            abstract=True


class Callout(TranslatableModel):
    callout_image = models.ImageField(_('Callout Image'),upload_to = storage.hashed_upload_to('callout_image'),null=True,blank=True)#default = 'images/None/default.jpg'

    translations = TranslatedFields(
       callout_title = models.CharField(_('Callout Title'),max_length=100, db_index=True)
    )

    class Meta:
        verbose_name = _('callout')
        verbose_name_plural = _('callouts')
        abstract = True

    def save(self, *args, **kwargs):
        try:
            this = Callout.objects.get(id=self.id).callout_image
            if this and this != self.callout_image:
                this.delete(save=False)
        except: pass
        super(Callout, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.callout_image:
            os.remove(self.callout_image.path)
        super(Callout, self).delete(*args, **kwargs)

class Map(TranslatableModel):
    map_link = models.CharField(_('Map Link'),max_length=300, db_index=True, blank=True, null=True)
    map_src = models.CharField(_('Map Source'),max_length=300, db_index=True, blank=True, null=True)
    translations = TranslatedFields(
       map_title = models.CharField(_('Map Title'),max_length=100, db_index=True,blank=True, null=True),
    )

    class Meta:
        verbose_name = _('map')
        verbose_name_plural = _('maps')
        abstract = True



class Onepage(CoreObject,Intro,Callout,Map):
    '''Landingpage'''
    image = models.ImageField(_('Landing Image'),upload_to = storage.hashed_upload_to('image'),null=True,blank=True)#default = 'images/None/default.jpg'

    translations = TranslatedFields(
        title = models.CharField(_('Landing Title'),max_length=100, db_index=True),
        landing_subtitle = models.CharField(_('Landing Subtitle'),max_length=100, db_index=True,blank=True,null=True),
    )

    class Meta:
        verbose_name = _('Onepage')
        verbose_name_plural = _('Onepage')

    def save(self, *args, **kwargs):
        try:
            this = Onepage.objects.get(id=self.id).image
            if this and this != self.image:
                this.delete(save=False)
        except: pass
        super(Onepage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Onepage, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.safe_translation_getter('title',)

### Services

class Services(CoreObject,TranslatableModel):

    SOCIAL_CHOICES=(
        ('legal','legal'),
        ('info','info'),
        ('users','users'),
        ('suitcase','suitcase'),
        ('university','university'),
        ('pencil','pencil'),
        ('rocket','rocket'),
    )
    display = models.CharField(max_length=20,choices=SOCIAL_CHOICES,default='rocket')


    #image = models.ImageField(_('Service Image'),upload_to = storage.hashed_upload_to('image'), null=True,blank=True)#default = 'images/None/default.jpg'
    translations = TranslatedFields(
        title = models.CharField(_('Service Title'),max_length=100, db_index=True),
        service_description = models.TextField(_('Service Description Field'),help_text=_('please insert some description here'),blank=True),
    )

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def save(self, *args, **kwargs):
        try:
            this = Services.objects.get(id=self.id).image
            if this and this != self.image:
                this.delete(save=False)
        except: pass
        super(Services, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Services, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.safe_translation_getter('title',)

class Portfolio(CoreObject,TranslatableModel):
    image = models.ImageField(_('Portfolio Image'),upload_to = storage.hashed_upload_to('image'), null=True,blank=True)#default = 'images/None/default.jpg'
    link = models.CharField(_('Portfolio Link'),max_length=300, db_index=True, blank=True, null=True)
    translations = TranslatedFields(
        title = models.CharField(_('Portfolio Title'),max_length=100, db_index=True),
    )

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')

    def save(self, *args, **kwargs):
        try:
            this = Social.objects.get(id=self.id)
            if this and this != self.image:
                this.delete(save=False)
        except: pass
        super(Portfolio, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Portfolio, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.safe_translation_getter('title','link')

#Contacts
class Phone(CoreObject):
    name = models.CharField(_('Name'),max_length=100,null=True,blank=True)
    number = models.CharField(_('Phone Number'),max_length=30)
    fax = models.CharField(_('Fax Number'),max_length=30, null=True,blank=True)

    class Meta:
        verbose_name = _('Phone Number')
        verbose_name_plural = _('Phone Numbers')

    def __unicode__(self):
        return u'%s: %s' % (self.last_update,self.number)

class Mail(CoreObject):
    mail = models.EmailField(_('Email Adress'),db_index=True)

    class Meta:
        verbose_name = _('Mail')
        verbose_name_plural = _('Mails')

class Contact(CoreObject,TranslatableModel):
    phone = models.ManyToManyField(Phone,blank=True, null=True,verbose_name=_('Phone'))
    plz = models.PositiveSmallIntegerField(_('PLZ'),max_length=10, blank=True, null=True)
    mail = models.ManyToManyField(Mail,blank=True, null=True,verbose_name=_('Mail'))

    translations = TranslatedFields(
        title = models.CharField(_('Contact Title'),max_length=100, db_index=True),
        country = models.CharField(_('Country'),max_length=100, db_index=True,null=True,blank=True),
        city = models.CharField(_('City'),max_length=100, db_index=True,null=True,blank=True),
        street = models.CharField(_('Street'),max_length=100, db_index=True,null=True,blank=True),
    )

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    #~ def __unicode__(self):
        #~ return u'%s' % (self.title,)

    def __unicode__(self):
        return self.safe_translation_getter('title',)

### Social
class Social(CoreObject,TranslatableModel):

    SOCIAL_CHOICES=(
        ('facebook','facebook'),
        ('twitter','twitter'),
        ('dribble','dribble'),
        ('google-plus','google-plus'),
        ('xing','xing'),
        ('linkedin','linkedin'),

    )
    network = models.CharField(max_length=20,choices=SOCIAL_CHOICES,default='facebook')
    translations = TranslatedFields(
        link = models.CharField(_('Social Link'),max_length=250, db_index=True),
        title = models.CharField(_('Social Title'),max_length=100, db_index=True),
    )

    class Meta:
        verbose_name = _('Social')
        verbose_name_plural = _('Socials')

    def save(self, *args, **kwargs):
        try:
            this = Social.objects.get(id=self.id)
            if this and this != self.image:
                this.delete(save=False)
        except: pass
        super(Social, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Social, self).delete(*args, **kwargs)

class SiteNotice(CoreObject,TranslatableModel):
    slug = models.SlugField(_('Slug'), unique_for_date='create_date',
                        help_text=_('A slug is a short name which uniquely identifies the item'))
    translations = TranslatedFields(
        title = models.CharField(_('Site-Notice Title'),max_length=250, db_index=True),
        content = models.TextField(_('Site-Notice Content'),help_text=_('please insert some description here'),blank=True),
    )

    class Meta:
        verbose_name = _('site notice')
        verbose_name_plural = _('site notice')

    def get_absolute_url(self):
        return self.slug

class DataPolicy(CoreObject,TranslatableModel):
    slug = models.SlugField(_('Slug'), unique_for_date='create_date',
                        help_text=_('A slug is a short name which uniquely identifies the item'))
    translations = TranslatedFields(
        title = models.CharField(_('Data Policy Title'),max_length=250, db_index=True),
        content = models.TextField(_('Data Policy'),help_text=_('please insert some description here'),blank=True),
    )

    class Meta:
        verbose_name = _('data policy')
        verbose_name_plural = _('data policy')

    def get_absolute_url(self):
        return self.slug

#News
class News(CoreObject):
    title = models.CharField(max_length=256,verbose_name=_('Title'))
    slug = models.SlugField(_('Slug'), unique_for_date='create_date',
                        help_text=_('A slug is a short name which uniquely identifies the item'))
    content = models.TextField(_('Content'),max_length=256,help_text=_('Please only short messages. You have only 256 chars'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-last_update', )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug
