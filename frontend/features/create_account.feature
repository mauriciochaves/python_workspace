
Feature: Creating an account

@debug
Scenario: Create an account sending all mandatory information 
        Given I am on Home Page
        And I click on sign in
        When I fill my email "kea@kea.com.br" on create an account field
        And I click on create an account
        Then I should go to "YOUR PERSONAL INFORMATION" screen
        #When I click on Mr title
        And I type "keakea" on first name
        And I type "junior" on last name
        And I type "123456" on password
        And I type "Seattle" on my address first name
        And I type "Los Angeles" on my address last name
        And I type "Barao de bonito" on address
        And I type "Recife" on city
        And I select "California" on state




        #And I click on register 
