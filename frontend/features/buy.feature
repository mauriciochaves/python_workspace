
Feature: Buy products

@debug
Scenario: When I try to buy a product without being logged in
        Given I am on Home Page
        And I click on Blouse
        And I click add to cart
        And I click proceed to checkout
        When I confirm the proceed to checkout 
        Then I should be redirect to authentication page
@debug
Scenario: Buy a product
        Given I am on Home Page
        And I click on sign in
        And I logged in
        And I go to home page 
        When I click on Blouse
        And I click add to cart
        And I click proceed to checkout
        And I confirm the proceed to checkout 
        And I click on proceed to checkout on address screen
        And I click on proceed to checkout on shipping screen


