Feature: AutomationPractice retrieve test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Retrieve password in AutomationPractice with valid credential
    Given The forget your password? link is clicked
    And Enter recover email "valid@email.com"
    When Retrieve Password link is clicked
    Then User successfully get the reset password to "valid@email.com"


  Scenario Outline: Unsuccessfully retrieve password reset email
    Given The forget your password? link is clicked
    And Enter recover_email "<recover_email>"
    When Retrieve Password link is clicked
    Then The "<fail_msg>" error message is shown
    Examples:
      | recover_email     | fail_msg                                                                 |
      |                   | Invalid email address.                                                   |
      | invalid.email.com | Invalid email address.                                                   |