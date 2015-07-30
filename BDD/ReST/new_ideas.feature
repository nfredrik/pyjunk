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
      |HTML   |text/html                        |
      | Cj    |application/json; charset=utf-8  |
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

Scenario: Create an individual resource
    Given I want to create a posts resource with an id of 9 and payload 1
    And the create succeeds
    Then I can verify the reply


Scenario: Basic resource request with validation
    Given I want to request a photo resource with an id of 1
    Then I can request it
    And the request succeeds
    And the response type is Cj
    And the Cj response has a url link


Scenario: Following links
    Given I want to request a photo resource with an id of 1
    Then I can request it
    Then I can request a the url link
    And I can find the png from the link response


  





 