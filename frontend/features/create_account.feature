
Feature: Creating an account

Scenario: Create an account sending all mandatory information 
        Given I am on Home Page
        And I click on sign in
        When I fill my email "keaaaa@keaaaaa.com.br" on create an account field
        And I click on create an account
        Then I should go to "YOUR PERSONAL INFORMATION" screen
        When I click on Mr title
        And I type "keakea" on first name
        And I type "Junior" on last name
        And I type "123456" on password
        And I type "Seattle" on my address first name
        And I type "Los Angeles" on my address last name
        And I type "Barão de Bonito" on address
        And I type "Recife" on city
        And I select "California" on state
        And I type "00000" on zip code
        And I type "9999999999" on mobile phone
        And I type "kea" on address alias
        And I click on register
        Then I should see my account information

Scenario: Create an account - without typing first name
        Given I am on Home Page
        And I click on sign in
        When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
        And I click on create an account
        Then I should go to "YOUR PERSONAL INFORMATION" screen
        When I click on Mr title
        And I type "Junior" on last name
        And I type "123456" on password
        And I type "Seattle" on my address first name
        And I type "Los Angeles" on my address last name
        And I type "Barão de Bonito" on address
        And I type "Recife" on city
        And I select "California" on state
        And I type "00000" on zip code
        And I type "9999999999" on mobile phone
        And I type "kea" on address alias
        And I click on register
        Then System should display the message "firstname is required."

Scenario: Create an account - without typing last name
        Given I am on Home Page
        And I click on sign in
        When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
        And I click on create an account
        Then I should go to "YOUR PERSONAL INFORMATION" screen
        When I click on Mr title
        And I type "keakea" on first name
        And I type "123456" on password
        And I type "Seattle" on my address first name
        And I type "Los Angeles" on my address last name
        And I type "Barão de Bonito" on address
        And I type "Recife" on city
        And I select "California" on state
        And I type "00000" on zip code
        And I type "9999999999" on mobile phone
        And I type "kea" on address alias
        And I click on register
        Then System should display the message "lastname is required."

Scenario: Create an account - without typing password
        Given I am on Home Page
        And I click on sign in
        When I fill my email "keaa@keaaaaaaaa.com.br" on create an account field
        And I click on create an account
        Then I should go to "YOUR PERSONAL INFORMATION" screen
        When I click on Mr title
        And I type "keakea" on first name
        And I type "Junior" on last name
        And I type "Seattle" on my address first name
        And I type "Los Angeles" on my address last name
        And I type "Barão de Bonito" on address
        And I type "Recife" on city
        And I select "California" on state
        And I type "00000" on zip code
        And I type "9999999999" on mobile phone
        And I type "kea" on address alias
        And I click on register
        Then System should display the message "passwd is required."
