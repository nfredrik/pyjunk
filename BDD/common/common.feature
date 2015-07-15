Feature: Try to implement functions that are common for both windows and Linux
         Use design patterns to make this testing as easy as possible

Scenario: List all files in a directory
    Given That current directory is "."
    Then Verify that one file is listed
    And We have a parent directory

Scenario: Get the MAC of the default network interface
    Given That we have a network interface
    Then Verify that we have MAC
    And Ping on own local IP-address
    
