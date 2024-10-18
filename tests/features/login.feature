@Login
Feature: Login

  Scenario: Verify if user is able to login with valid user
    Given User navigates to login page
    When User enters username as 'standard_user'
    And User enters password for 'standard_user'
    And User clicks on 'Login' button
    Then Homepage is displayed
    And Labels are present
      | label_name |
      | Products   |

  Scenario Outline: Verify if user is able to login with '<username>'
    Given User navigates to login page
    When User enters username as '<username>'
    And User enters password for '<username>'
    And User clicks on 'Login' button
    Then Homepage is displayed
    Examples:
      | username                |
      | performance_glitch_user |
      | error_user              |
      | locked_out_user         |