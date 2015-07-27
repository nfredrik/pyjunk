@test
Feature: Basic REST Interactions
    Try to use a new way to test the rest API

Background:
  Given the server knows about the following resources
      |type   |path                    |
      |posts  |/posts                  |
      |post  |/posts/{id}              |
      |nonexistent|/hue/does/not/exist |
 
And the server knows about the following mime types
      |HTML   |text/html                       |
      |Cj     |application/vnd.collections+json|

Scenario: Basic resource request
    Given I want to interact with an posts resource
    Then I can request it


Scenario: Work with an individual resource
    Given I want to request a post resource with an id of 7
    And the request succeeds
    Then I can read it's content







 