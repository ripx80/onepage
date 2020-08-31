from lxml.html.clean import clean_html
import lxml
from lxml.html.clean import Cleaner
#parser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
from lxml.html import tostring, html5parser


from html5lib.html5parser import HTMLParser
from html5lib import treebuilders
from django.http import HttpResponse


class ValidateMiddleware(object):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if response.content and 'html' in response['Content-Type'] \
                and 'disable-validation' not in request.GET:
            # validate
            treebuilder = treebuilders.getTreeBuilder("etree")
            parser = HTMLParser(tree=treebuilder, strict=True)

            try:
                parser.parse(response.content)
            except Exception:
                pass
            if parser.errors:
               print(parser.errors)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        return callback(request, *callback_args, **callback_kwargs)



class PrettifyMiddleware(object):
    """Prettify middleware"""

    def process_response(self, request, response):
        if response['Content-Type'].split(';', 1)[0] == 'text/html':
            content=response.content
            #html=lxml.html.fromstring(content)

            #print(lxml.html.tostring(html))


            content=tostring(html5parser.fromstring(content))


            #cleaner = Cleaner(style=False,page_structure=False, links=False,comments=True,meta=False)
            #cleaner = Cleaner(style=False, links=True, add_nofollow=True,page_structure=False, safe_attrs_only=False)

            #content=cleaner.clean_html(content)
            #content=clean_html(content)




                #send cleaned document back

            #response.content = document

            #print(errors)
            response.content = content
        return response
