Feature: As a newbie of BDD and ReST
  I wish to understand how Behaviour Driven Development, BDD,  and
  Representational State Transfer, REST, works

  I will write an couple of scenarios and use jsonplaceholder as server
  to handle to the interaction with this client and the server

  Background:
    Given I am using the client trying to setup a conversation with a rest service using some resources

  Scenario: List the allowed operations on a resource
     Given I ask for supported operations on a resource 
     Then I will get a reply on supported operations
     
  Scenario: Show a specific resource
     Given I want to retrieve the information about resource "1"
     Then I should see json information about resource "1"

 Scenario Outline: Show and arbitrary resource 
     Given I want to retrieve the information about resource "<id>"
     Then I should see json information about resource "<id>"
   
   Examples:
    | id        | 
    | 1         |  
    | 45        |
    | 100       | 
   
   Scenario: List all possible resources
     Given I want to retrieve the information about all resources
     Then I should see a list of json information


   Scenario: Handle a non-existing resource
       Given I try to retrieve a non existing resource
       Then  It throws a KeyError exception



     