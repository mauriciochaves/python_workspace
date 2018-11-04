
Feature: Test Api

  Scenario Outline: since I want to register a new user
    Given I send POST request on resource url "/api/register" using: "<email>" value to "email" field, "<password>" value to "password" field
    When I retrieve the results
    Then the status code should be 201
    And it should have the field "token" containing the not empty value
    Examples:
    |email|password|
    |teste2_mcsj@test.com|teste12345|

  Scenario Outline: since I do not enter the password at the time of registration
    Given I send POST request on resource url "/api/register" using: "<email>" value to "email" field
    When I retrieve the results
    Then the status code should be 400
    And it should have the field "error" containing the value "Missing password"
    Examples:
    |email|
    |teste_error@test.com|

  Scenario Outline: since I need to create a new user
    Given I send POST request on resource url "/api/users" using: "<name>" value to "name" field, "<job>" value to "job" field
    When I retrieve the results
    Then the status code should be 201
    And it should have the field "id" containing the not empty value
    And it should have the field "name" containing the value "<name>"
    And it should have the field "job" containing the value "<job>"
    Examples:
    |name|job|
    |Mauricio|Junior Test Engineer|

  Scenario Outline: since I need to fill in the user's job information
    Given I send POST request on resource url "/api/users" using: "<name>" value to "name" field, "<job>" value to "job" field
    And I retrieve value of the parameter "id" from results
    When I send PUT request on resource url "/api/users/" using: "<name>" value to "name" field, "<new_job>" value to "job" field
    And I retrieve the results
    Then the status code should be 200
    And it should have the field "name" containing the value "<name>"
    And it should have the field "job" containing the value "<new_job>"
    Examples:
    |name|job|new_job|
    |Mauricio|Junior Test Engineer|Full Test Engineer|

  Scenario: since I need to get only one user
    Given I send GET request on resource url "/api/users/2"
    When I retrieve the results
    Then the status code should be 200
    And it should have the field "id" containing the value "2" in "data" field

  Scenario: since I inform an unregistered user
    Given I send GET request on resource url "/api/users/777"
    When I retrieve the results
    Then the status code should be 404

