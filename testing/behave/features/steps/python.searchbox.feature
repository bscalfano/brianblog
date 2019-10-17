Feature: Searchbox correctly searches for items

Scenario: Display a no result message when there are no results 
    Given we have a browser looking at "http://www.python.org"
    When we search for "lasdjfghklhfdkj"
    Then we get a "No Results" message

Scenario: Display a no result message when there are no results 
    Given we have a browser looking at "http://www.python.org"
    When we search for "x$12asdfg345"
    Then we get a "No Results" message

Scenario:Don't Display a no result message when there are results 
    Given we have a browser looking at "http://www.python.org"
    When we search for "pycon"
    Then we don't get a "No Results" message