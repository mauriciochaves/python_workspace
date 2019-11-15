# language:en

Feature: Login

   Background: SETUP
        Given I register an user with email folowing data
        |email                                   |password  |
        |mauricio.chaves.junior@live.com         |123456    |
        |mauricio.chaves.silva.junior@gmail.com  |123456    |


   Scenario: Login successful - post without token
        Given I login with email "eve.holt@reqres.in" and "cityslicka"
        Then I verify that status code is "200"


   Scenario: Login unsuccessful
        Given I login only with email "mauricio.chaves.silva.junior@gmail.com"
        Then I verify that status code is "400"
        And I verify that response contains "Missing password" as "error" attribute 