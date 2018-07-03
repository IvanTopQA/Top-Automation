Feature: QA middle page

Background:
    Given we are on QA-engineer page

Scenario: Check title of the page
    Then we see "QA-engineer" in the title

Scenario: Check if tab buttons are clickable
    Then we see that tabs' buttons are clickable

Scenario: Check text in each tab
    Then we see correct text in each tab

Scenario: Check that checkboxes are not clickable
    Then we see that checkboxes are not clickable

Scenario: Check link "Софт для быстрого создания скриншотов"
    When we go to the second tab
    And we click link "Софт для быстрого создания скриншотов"
    Then we are on http://monosnap.com/