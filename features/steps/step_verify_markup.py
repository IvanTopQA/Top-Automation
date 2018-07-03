#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then


@given('we are on QA-engineer page')
def step_impl(context):
    context.qa_page.navigate(context.driver)
    context.qa_page.at(context.driver)


@then('we see {title} in the title')
def step_impl(context, title):
    assert title in context.qa_page.get_title(context.driver)


@then('we see that tabs\' buttons are clickable')
def step_impl(context):
    context.qa_page.check_buttons_clickable(context.driver)


@then('we see correct text in each tab')
def step_impl(context):
    context.qa_page.check_texts_in_tabs(context.driver)


@then('we see that checkboxes are not clickable')
def step_impl(context):
    context.qa_page.check_if_checkboxes_are_clickable(context.driver)


@when('we go to the {tab} tab')
def step_impl(context, tab):
    context.qa_page.click_tab(context.driver, tab)


@when('we click link "{link}"')
def step_impl(context, link):
    context.qa_page.click_link(context.driver, link)


@then('we are on {link}')
def step_impl(context, link):
    context.qa_page.wait_for_window_open(context.driver, link)
    assert "http://monosnap.com/" in context.driver.current_url