# -*- coding: utf-8 -*-

from selenium import webdriver
from pages.qa_page import QaPage
import selenium.webdriver.support.ui as ui
import datetime
import time


def get_date_time():
    dt_format = '%Y%m%d_%H%M%S'
    return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)


def before_all(context):
    context.base_url = "http://blog.csssr.ru"
    context.driver = webdriver.Chrome()
    context.wait = ui.WebDriverWait(context.driver, 15)
    context.qa_page = QaPage(context)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot('artifacts/' + scenario.name + get_date_time() + "_failed.png")
        file = open('artifacts/' + scenario.name + get_date_time() + '.html', 'w')
        file.write(context.driver.page_source)
        file.close()


def after_all(context):
    context.driver.quit()
