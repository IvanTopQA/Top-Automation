# -*- coding: utf-8 -*-

from .base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from texts.texts import *

class QaPage(Page):

    class wait_url_to_contain(object):
        def __init__(self, _text):
            self.text = _text

        def __call__(self, driver):
            return self.text in driver.current_url

    url = '/qa-engineer/'

    buttons_tabs = ["ВНИКАТЬ В ДЕТАЛИ ПРОЕКТОВ",
                    "НАХОДИТЬ НЕСОВЕРШЕНСТВА",
                    "СОПРОВОЖДАТЬ ПРОЕКТЫ",
                    "РАБОТАТЬ С ФАЙЛАМИ ПРОЕКТОВ"]

    def get_title(self, driver):
        return driver.title


    def check_buttons_clickable(self, driver):
        for button in QaPage.buttons_tabs:
            self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="'+button+'"]')))
            self.context.driver.find_element_by_xpath('//a[text()="'+button+'"]').click()


    def check_texts_in_tabs(self, driver):
        for button in QaPage.buttons_tabs:
            self.context.driver.find_element_by_xpath('//a[text()="'+button+'"]').click()
            for tab_text in texts_in_tabs:
                assert tab_text in self.context.driver.find_element_by_xpath('//h1[contains(text(), "'+tab_text+'")]').text


    def check_if_checkboxes_are_clickable(self, driver):
        for button in QaPage.buttons_tabs:
            self.context.driver.find_element_by_xpath('//a[text()="' + button + '"]').click()
            self.context.wait.until_not(EC.element_to_be_clickable((By.XPATH, '//input')))


    def click_tab(self, driver, tab):
        if tab == "first":
            self.context.driver.find_element_by_xpath('//a[text()="' + QaPage.buttons_tabs[0] + '"]').click()
        elif tab == "second":
            self.context.driver.find_element_by_xpath('//a[text()="' + QaPage.buttons_tabs[1] + '"]').click()
        elif tab == "third":
            self.context.driver.find_element_by_xpath('//a[text()="' + QaPage.buttons_tabs[2] + '"]').click()
        elif tab == "fourth":
            self.context.driver.find_element_by_xpath('//a[text()="' + QaPage.buttons_tabs[3] + '"]').click()


    def click_link(self, driver, link):
        self.context.driver.find_element_by_xpath('//a[text()="'+link+'"]').click()


    def wait_for_window_open(self, driver, link):
        self.context.wait.until(QaPage.wait_url_to_contain(link))
