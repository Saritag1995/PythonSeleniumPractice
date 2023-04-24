Feature: Login and verify amazon.com website

  @amazonLoginTest
  Scenario: Verify Amazon login functionality
    Given the user opens google
    When the user enters url
    Then user enter username and password
    Then user clicks on sign in button
    Then user verify home page

  @amazonSearchTest
  Scenario: Verify search functionality
    Given the user opens google
    When the user enters url
    Then user enter username and password