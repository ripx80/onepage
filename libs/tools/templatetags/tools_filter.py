#import markdown2 as markdown
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markcode(value):
    return mark_safe(markdown.markdown(force_unicode(value),extensions=['codehilite']))

    #return mark_safe(markdown2.markdown(force_unicode(value),extras=['fenced-code-blocks']))
    #for markdown2 you only used ``` for code beginning. Its faster.
register.filter('markcode', markcode)

@register.filter(name='addcss')
def addattr(value, arg):
    if value.css_classes():
        arg=arg+' '+value.css_classes
    return value.as_widget(attrs={'class': arg})

@register.filter(name='addtitle')
def addattr(value, arg):
    return value.as_widget(attrs={'title': arg})
