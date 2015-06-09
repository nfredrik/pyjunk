Feature: Wikipedia search
  In order to find information
  As a Wikipedia user
  I want to search on different subjects

  Scenario: Searching for one specific subject
    Given I can access Wikipedia
    When I search for "Capybara"
    Then I get a result for "Capybara"

  Scenario Outline: Searching for several subjects
    Given I can access Wikipedia
    When I search for <subject>
    Then I get a result for <subject>
    And I find relevant information on <subject>
  Examples:
    | subject   |
    | Capybara  |
    | Selenium  |

  Scenario Outline: Searching without repeating subject
    Given I can access Wikipedia
    When I search for the subject "<subject>"
    Then I get a matching result
    And I find relevant information
  Examples:
    | subject   |
    | Capybara  |
    | Selenium  |