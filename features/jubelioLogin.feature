Feature: Jubelio Login

  Scenario: Login to Jubelio with valid parameters
    Given Launch chrome browser
    When I am on the www.app.jubelio.com Login Page
    And Fill email field with "qa.rakamin.jubelio@gmail.com" and fill password with "Jubelio123!"
    And Click on Masuk button
    Then User must successfully login to the Home Page

  Scenario Outline: Login to Jubelio with multiple parameters
    Given Launch chrome browser
    When I am on the www.app.jubelio.com Login Page
    And Fill email field with "<email>" and fill password with "<password>"
    And Click on Masuk button
    Then User must successfully login to the Home Page

    Examples:
    | email                         | password    |
    | qa.rakamin.jubelio@gmail.com  | Jubelio123! |
    | aa.rakamin.jubelio@gmail.com  | admin       |




