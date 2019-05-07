Feature: Showing off behave

  Scenario: 
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first operand
    And we have [[1, 1], [3, 3]] as second operand
    Then the result should be [[2, 2], [5, 5]]