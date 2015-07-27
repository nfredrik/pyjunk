Feature: Even more stuff



Scenario: Resource doesn't exist
    Given I want to interact with a nonexisting resource
    Then I can request it
    And the will not be found

Scenario: Content Negotiation to known type
    Given I want to interact with an posts resource
    Then I can request it as HTML
    And the request succeds
    And the response type is HTML

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

