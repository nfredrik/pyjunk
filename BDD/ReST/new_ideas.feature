@test
Feature: Basic REST Interactions
    Try to use a new way to test the rest API

Background:
  Given the server knows about the following resources
      |type       | path                |
      |posts      | /posts              |
      |post       | /posts/{id}         |
      |nonexistent| /hue/does/not/exist |
      |photo      | /photos/{id}         |
 
And the server knows about the following mime types
      | type  | path                            | 
      |HTML   |text/html                        |
      | json  |application/json; charset=utf-8  |
      | png   | image/png                       |

And the server knows the structure of the payload
      | payload | title  | body | userId |
      |   1     | foo    | bar  |   1    |
      |   2     | nisse  | pelle|   2    |


Scenario: Basic resource request
    Given I want to interact with an posts resource
    Then I can request it


Scenario: Work with an individual resource
    Given I want to request a post resource with an id of 7
    And the request succeeds
    Then I can read it's content

@create
Scenario: Create an individual resource
    Given I want to create a posts resource with an id of 9 and payload 1
    And the create succeeds
    Then I can verify the reply

@update
Scenario: Update an existing resource
    Given I want to update a post resource with an id of 9
    And the update succeeds
    And I will get a confirmation that resource has been updated

@delete
Scenario: Delete an individual resource
    Given I want to delete a post resource with an id of 1
    And the delete succeeds
    Then I can verify the deletion





Scenario: Basic resource request with validation
    Given I want to request a photo resource with an id of 1
    Then I can request it
    And the request succeeds
    And the response type is json
    And the Cj response has a url link


Scenario: Following links
    Given I want to request a photo resource with an id of 1
    Then I can request it
    Then I can request a the url link
    And I can find the png from the link response

Scenario: Resource doesn't exist
    Given I want to interact with an nonexistent resource
    Then I can request it
    And the request will not be found

@html
Scenario: Content Negotiation to known type
    Given I want to interact with an posts resource
    Then I can request it as HTML
    And the request succeeds
    And the response type is HTML

@json
Scenario: Content Negotiation to other known type
    Given I want to interact with an posts resource
    Then I can request it as json
    And the request succeeds
    And the response type is json

  





 