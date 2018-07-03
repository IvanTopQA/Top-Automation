# -*- coding: UTF-8 -*-


class Page(object):

    url = None
    context = None

    def __init__(self, context):
        self.context = context

    def navigate(self, driver): # navigate to the page url
        driver.get(self.context.base_url+self.url)

    def at(self, driver): # assert urls
        return self.context.base_url + self.url == driver.current_url