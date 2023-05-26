# Created by Srk at 5/24/2023
  Feature: Verify if Book are added and deleted successfully using Library API
  # Enter feature description here

  Scenario: Verify AddBook API Functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then the Book is Successfully added
