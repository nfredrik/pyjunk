Feature: As a newbie of BDD and ReST continue
  I continue my journey to understand BDD and rest. In this feature
  I focus on adding, updating and deleting and try to cover
  fault scenarios aswell. Try to verify that some methods are idempotent

Background:
    Given I am using the client trying to setup a conversation with a rest service using some resources


Scenario: Add a new resource
    Given I order to create a new resource "1"
    Then  get an "CREATED" in the reply
    And   I will get a confirmation that resource "1" has been created

   Scenario: Update an existing resource
    Given I order to update resource "1"
    Then  get an "OK" in the reply
    And   I will get a confirmation that resource "1" has been updated

   Scenario: Add a already existing resource


   Scenario: Partial update an existing resource
    Given I order a partial update of resource "1"
    Then get an "BAD_REQUEST" in the reply
    And  some information in return     


   Scenario: Delete a existing resource. Today with get "OK" as reply but it should be "NO_CONTENT"
    Given I order to delete resource "1"
    Then  get an "OK" in the reply

   Scenario: Delete a non-existing resource
    Given I order to delete resource "501"
    Then  get an "OK" in the reply

   Scenario: Partial update an non-existing resource
    Given I order a partial update of resource "4"
    Then get an "BAD_REQUEST" in the reply
    And  some information in return     

   Scenario: Quickly check whether a resource exists on the server or not, no data just metadata
   Given I want to know if "2" exists as a resource 
    Then get an "OK" in the reply   
    But  I will get metadata as reply





   Scenario: Update an non-existing resource

   Scenario: Partial update an non-existing resource



