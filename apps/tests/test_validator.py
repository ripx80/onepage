# -*- coding: utf-8 -*-
import re
#~ from lettuce import world, step, before
#~ from lettuce_webdriver.util import find_field
#~ from lettuce_webdriver import webdriver # We need this to register "I visit..."
#~ from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def check_html_valid()
    world.browser = webdriver.Firefox()
    profile = FirefoxProfile()

    #slow down
    # When inserting many lines of text the Javascript process takes ages
    profile.set_preference('dom.max_script_run_time', 10*60)
    profile.set_preference('dom.max_chrome_script_run_time', 10*60)
    world.slow_browser = webdriver.Firefox(firefox_profile=profile)


        page_source = world.browser.page_source
        # Fix doctype which Firefox & validator disagree upon
        page_source = re.sub(u"^<!DOCTYPE HTML ", u"<!DOCTYPE html ", page_source)

        # Post to validator
                world.slow_browser.get("http://validator.w3.org/#validate_by_input")
        field = find_field(world.slow_browser, 'textarea', 'fragment')
        field.clear()
        field.send_keys(page_source)
        field.submit()
        assert_true("Congratulations" in world.slow_browser.page_source)



