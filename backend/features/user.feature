# language:en

Feature: User

    Background: SETUP
        Given I prepare environment for tests run


    Scenario: Create employee - post with token
        When I register an employee with name "morpheus" and job "leader"
        Then I verify that status code is "201"
        And I verify that response contains "morpheus" as "name" attribute
        And I verify that response contains "leader" as "job" attribute


    Scenario: Change employee- put with token
        Given I register an employee with name "morpheus" and job "leader"
        When I change an employee 1 with name "morpheus" and job "zion resident"
        Then I verify that status code is "200"
        And I verify that response contains "zion resident" as "job" attribute


    Scenario: Delete employee- delete with token
        Given I register an employee with name "morpheus" and job "leader"
        When I delete the employee 1
        Then I verify that status code is "204"


    Scenario: Search employee- search with token
        Given I register an employee with name "morpheus" and job "leader"
        When I search the employee 1
        Then I verify that status code is "200"


    Scenario: Try to search an employee that does not exist 
        When I search the employee -1
        Then I verify that status code is "404"


    Scenario: Try to create an user without using a password
        When I try to register an user using only email "kea@gmail.com"
        Then I verify that status code is "400"
        And I verify that response contains "Missing password" as "error" attribute


    Scenario Outline: Search employee list - search with token
        Given I register an employee with name <name> and job <job>
        When I get employee list with page <page>
        Then I verify that status code is "200"


        Scenarios: Platinum Client
        | name      | job            | page  |
        | Morpheus  | leader         | 2     |
        | John      | zion resident  | 3     |
        | Maven     | Engineer       | 4     |


        Scenarios: Gold Client
        | name       | job            | page  |
        | Jack       | leader         | 5     |
        | Lit        | zion resident  | 6     |
        | Marvel     | Engineer       | 7     |