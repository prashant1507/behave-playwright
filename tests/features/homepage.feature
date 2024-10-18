@Homepage
Feature: Homepage

  Background:
    Given User navigates to login page

  Scenario: Verify if user is able to see 'Swag Labs' on login
    When User enters username as 'problem_user'
    And User enters password for 'problem_user'
    And User clicks on 'Login' button
    Then Homepage is displayed

  Scenario: Verify if user is able to see 'Swag Labs' on login
    When User enters username as 'problem_user'
    And User enters password for 'problem_user'
    And User clicks on 'Login' button
    Then Homepage is displayed

  Scenario: This is failed test case
    When User enters username as 'problem_user'
    And User enters password for 'problem_user'
    And User clicks on 'Login' button
    Then Product is displayed