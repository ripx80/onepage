from classytags.helpers import InclusionTag
from django import template
from django.template.loader import render_to_string

register = template.Library()

class CookieBanner(InclusionTag):
    """
    Displays cookie banner only if user has not dismissed it yet.
    """
    template = 'cookie_banner/banner.html'

    def render_tag(self, context, **kwargs):
        template = self.get_template(context, **kwargs)
        if context['request'].COOKIES.get('mtcookies', False):
            return ''
        data = self.get_context(context, **kwargs)
        return render_to_string(template, data)

register.tag('get_cookie_banner',CookieBanner)
