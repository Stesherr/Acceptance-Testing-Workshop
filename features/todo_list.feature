Feature: To-do list
    Scenario: Add a task to the to-do list
        Given list is empty
        When the user enters the task "study"
        Then the list must contain "study"
    
    Scenario: List all tasks in the to-do list
        Given the list has at least one element
        When the user chooses option "2"
        Then the list size is greater than zero

    Scenario: Mark a task as completed
        Given the list has four elements
        When the user takes option "3"
        When the user chooses task "2"
        Then the list no longer contains task "2"

    Scenario: Clear the entire to-do list
        Given the list has one or more elements
        When the user picks up option "4"
        Then the size of the list is zero

    Scenario: Rename a task
        Given the list has five elements
        When the user selects option "5"
        When the user go for task "2"
        When the user enters the name "program"
        Then the task in "2" has the name "program"