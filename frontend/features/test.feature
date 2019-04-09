
Feature: Registering a tester


Scenario: when I try to login 
        Given I am on Home Page
        When I fill in the email field with the "mcsj123@teste.com" who is not registered
        Then system should display the message "Password is required."