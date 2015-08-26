@new
Feature: Basic REST Interactions
    Try to use a new way to test the rest API

    As a    REST API Client 
    I want to verify all possible methods that a server provides
    So that I'm confident that the API will be intact when 
    regression testing later on


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

Scenario: Supported methods by server
    Given I want to know supported methods
    When I ask for it
    Then I will get it as metadata
    And It will be set or subset of the RestAPI

Scenario: Verify a resource existence
    Given Me want to interact with a post resource with an id of 1
    When  Check for it's existance
    Then I will get it
    And check that the metadata is valid

Scenario: Basic resource request
    Given Me want to interact with a post resource with an id of 1
    When I request it
    Then I will get it
    And can verify the content

Scenario: Delete a resource
    Given Me want to interact with a post resource with an id of 1
    When I delete it
    Then I will get it