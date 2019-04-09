Feature: Login

   Background: SETUP
        Given I register an user with email "mauricio.chaves.junior" and "123456"


   Scenario: Login successful - post without token
        Given I login with email "mauricio.chaves.junior" and "123456"
        Then I verify that status code is "200"


   Scenario: Login unsuccessful
        Given I login with email "mauricio.chaves.junior"
        Then I verify that status code is "400"