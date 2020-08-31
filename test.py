# -*- coding: utf-8 -*-
from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from django.conf import settings
from importlib import import_module
from html5lib.html5parser import HTMLParser
from html5lib import treebuilders
#import lxml
from libs.tools.helper import w3c_client

#Third-party app imports
#look at this
from model_mommy import mommy



class UrlsAliveTest(TestCase):
    ''' Testing Status Code of the url and can validate the dom and the html.
        Use W3C Validator to validate HTML.
        Get all URLS from the installed APPS and check them.
        Skipping URLS where need kwargs. You must specifiy them.
        Overwrite Settings DEBUG to FALSE, because this not working if debug_toolbar
        is enabled.
    '''


    def setUp(self):
        """
        Set up all the tests
        """
        self.onepage = mommy.make('onepage',title='TEST')
        print(self.onepage)



    @override_settings(DEBUG=False)
    def test_responses(self):
         #from apps.onepage.models import Onepage


        allowed_http_codes=[200, 302, 403, 405]#clean forbitten from this
        credentials={'username': 'john', 'password': 'smith'}
        logout_url="/logout/"
        use_w3c=True
        quiet=False
        debug=False
        default_kwargs={}

        module = import_module(settings.ROOT_URLCONF)
        if credentials:
            self.client.login(**credentials)

        def validate_url(self,url,use_w3c=True,quite=True):
            'validate urls with the w3c validator. Need an Internet Connection'

            client=Client()
            response = client.get(url,follow=True)
            if response.status_code==200:
                src=response.content
                treebuilder = treebuilders.getTreeBuilder("etree")
                parser = HTMLParser(tree=treebuilder, strict=True)
                try:
                    parser.parse(src)
                except Exception as ex:
                    pass

                if not parser.errors and use_w3c:
                    #uploading to w3c
                    w3c=w3c_client(src)
                    if w3c and not w3c[0]:
                        print('%s: %s'%(url,w3c[1],))
                        if not quite:
                            for i in w3c[2]['messages']:
                                print(i['messageid'])
                                print('\t%s'%(i['message'],))
                        #self.assertTrue(w3c[0])
            else:
                print('skipping html check %s',(response.status_code,))


        def check_urls(urlpatterns, prefix=''):
            'get all urls from urls.py and check them'
            for pattern in urlpatterns:
                if hasattr(pattern, 'url_patterns'):
                    # this is an included urlconf
                    new_prefix = prefix
                    if pattern.namespace:
                        new_prefix = prefix + (":" if prefix else "") + pattern.namespace
                    check_urls(pattern.url_patterns, prefix=new_prefix)

                params = {}
                skip = False
                redirects=False
                regex = pattern.regex

                if regex.groups > 0:
                    # the url expects parameters
                    # use default_kwargs supplied
                    if regex.groups > len(regex.groupindex.keys()) \
                        or set(regex.groupindex.keys()) - set(default_kwargs.keys()):
                        # there are positional parameters OR
                        # keyword parameters that are not supplied in default_kwargs
                        # so we skip the url
                        skip = True
                    else:
                        for key in set(default_kwargs.keys()) & set(regex.groupindex.keys()):
                            params[key] = default_kwargs[key]

                if hasattr(pattern, "name") and pattern.name:
                    name = pattern.name
                else:
                    # if pattern has no name, skip it
                    skip = True
                    name = ""
                fullname = (prefix + ":" + name) if prefix else name

                if not skip:
                    url = reverse(fullname, kwargs=params)
                    response = self.client.get(url)
                    self.assertIn(response.status_code, allowed_http_codes)
                    if response.status_code == 200:
                        validate_url(self,url,use_w3c,quiet)

                    status = "" if response.status_code == 200 else str(response.status_code) + " "
                    if not quiet:
                        if response.status_code != 302:
                            print(status + url)
                        elif redirects:
                            print(status + url)

                    if url == logout_url and credentials:
                        # if we just tested logout, then login again
                        self.client.login(**credentials)
                else:
                    if debug:
                        print("SKIP " + regex.pattern + " " + fullname)
        check_urls(module.urlpatterns)
