Feature: SignIn as passenger
  In order to use kapten web application,
  As a passenger
  I need to be able to signin

  Scenario: Successful signin
    Given user opens signin page
     When user sign in with "riabinina@selenium.com" email and "Qwe123456" password
     Then user is logged in
      And "commander" is in url

  Scenario: SignIn with invalid credentials
    Given user opens signin page
     When user sign in with "riabinina@selenium.com" email and "Qwe111111" password
     Then user sees error message


