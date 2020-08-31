from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Url, Rule



class RuleAdminForm(forms.ModelForm):
    class Meta:
        model = Rule
        exclude = []
    def clean(self):
        if (not self.cleaned_data.get("disallowed", False) and
                not self.cleaned_data.get("allowed", False)):
            raise forms.ValidationError(
                _('Please specify at least one allowed or dissallowed URL.'))
        return self.cleaned_data

class RuleAdmin(admin.ModelAdmin):
    form = RuleAdminForm
    fieldsets = [
        (None, {'fields': ['robot', 'sites']}),
        (_('URL patterns'),{'fields': ['allowed', 'disallowed']}),
        (_('Advanced options'), {'classes': ('collapse',),
            'fields': ['crawl_delay',],
        }),
    ]

    list_filter = ('sites',)
    list_display = ('robot','allowed_urls','disallowed_urls')
    search_fields = ('robot', 'urls')
    filter_horizontal = ('allowed','disallowed')

class UrlAdmin(admin.ModelAdmin):

    list_display = ('pattern',)
    search_fields = ('pattern',)

admin.site.register(Url,UrlAdmin)
admin.site.register(Rule, RuleAdmin)
