Feature: Login

   Background: SETUP
        Given I register an user with email folowing data
        |email                                   |password  |
        |mauricio.chaves.junior@live.com         |123456    |
        |mauricio.chaves.silva.junior@gmail.com  |123456    |

   @mcsj
   Scenario: Login successful - post without token
        Given I login with email "mauricio" and "123456"
        Then I verify that status code is "200"


   Scenario: Login unsuccessful
        Given I login with email "chaves"
        Then I verify that status code is "400"