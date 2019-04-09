Feature: Login

    Background: SETUP
        Given I register an user with email "mauricio.chaves.junior" and "123456"
        And I login with email "mauricio.chaves.junior" and "123456"


    Scenario: Create employee - post with token
        When I register an employee with name "morpheus" and job "leader"
        Then I verify that status code is "201"


    Scenario: Change employee- put with token
        Given I register an employee with name "morpheus" and job "leader"
        When I change an employee 1 with name "morpheus" and job "zion resident"
        Then I verify that status code is "200"


    Scenario: Delete employee- delete with token
        Given I register an employee with name "morpheus" and job "leader"
        When I delete the employee 1
        Then I verify that status code is "204"


    Scenario: Search employee- search with token
        Given I register an employee with name "morpheus" and job "leader"
        When I search the employee 1
        Then I verify that status code is "200"


    Scenario: Search employee list- search with token
        Given I register an employee with name "morpheus" and job "leader"
        When I get employee list with page "2"
        Then I verify that status code is "200"