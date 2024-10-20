@Login
Feature: Login

  @QA-9 @xx
  Scenario: Verify if user is able to login with valid user
    Given User navigates to login page
    When User enters username as 'standard_user'
    And User enters password for 'standard_user'
    And User clicks on 'Login' button
    Then Homepage is displayed
    And Labels are present
      | label_name |
      | Products   |

  @QA-6 @xx
  Scenario: Verify if user is able to login with 'performance_glitch_user'
    Given User navigates to login page
    When User enters username as 'performance_glitch_user'
    And User enters password for 'performance_glitch_user'
    And User clicks on 'Login' button
    Then Homepage is displayed

  @QA-7 @QA-8
  Scenario Outline: Verify if user is able to login with '<username>'
    Given User navigates to login page
    When User enters username as '<username>'
    And User enters password for '<username>'
    And User clicks on 'Login' button
    Then Homepage is displayed
    Examples:
      | username                |
      | error_user              |
      | locked_out_user         |