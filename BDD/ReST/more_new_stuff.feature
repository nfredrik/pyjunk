Feature: Even more stuff


Scenario: Basic resource request with validation
    Given I want to interact with an posts resource
    Then I can request it
    And the request succeeds
    And the response type is Cj
    And the Cj response has a bridge link
    And the Cj response has a light link

Scenario: Following links
    Given I want to interact with an posts resource
    Then I can request it
    Then I can request a the bridge link
    And I can find the id from the link response
    And I can find the internalipaddress from the link response

