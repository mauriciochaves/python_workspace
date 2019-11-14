
Feature: Registering a tester

Scenario: When I try to login 
        Given I am on Home Page
        And I click on sign in
        When I fill in the email field with the "mcsj123@teste.com" who is not registered
        Then System should display the message "Password is required."

