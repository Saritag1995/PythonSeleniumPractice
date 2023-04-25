Feature: Login and verify amazon.com website

  @amazonLoginTest
  Scenario: Verify Amazon login functionality
    Given the user enters url
    When clicks on sign in link
    Then user enter username and password
    Then user clicks on sign in button
    Then user verify home page

  @amazonSearchTest
  Scenario: Verify search functionality
    Given the user searches an item
    When the user clicks on search button
    Then user click on searched item