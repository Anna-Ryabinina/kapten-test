Feature: SignUp as passenger
  In order to use kapten web application,
  As a passenger
  I need to be able to signup

  Scenario: Successful signup
    Given user opens signup page
     When user sign up with new valid credentials
     Then user is registered
      And "validate_phone" is in url

