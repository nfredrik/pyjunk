Feature: As a writer for Acme
  I wish to demonstrate
  How easy writing Acceptance Tests
  In Python really is.

  Background:
    Given I am using the calculator

  Scenario: Calculate 2 plus 2 on our calculator
     Given I input "2" add "2"
     Then I should see "4"

  Scenario Outline: Calculate addent1 plus addent2 on our calculator
     Given I input "<addent1>" add "<addent2>"
     Then I should see "<result>"
   
   Examples:
    | addent1   | addent2  | result |
    | 2         |  2       |   4    |
    | 3         |  2       |   5    | 
    | 3         |  3       |   6    |
    | 3         |  97      |  100   |     