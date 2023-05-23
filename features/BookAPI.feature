# Created by Srk at 5/23/2023
Feature: Verify if the Books are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is Successfully added