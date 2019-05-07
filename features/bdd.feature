Feature: Matrix Calculator testing

  Scenario: Add two matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first operand
    And we have [[1, 1], [3, 3]] as second operand
    Then the add result should be [[2, 2], [5, 5]]

  Scenario: Diff two matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first operand
    And we have [[1, 1], [3, 3]] as second operand
    Then the diff result should be [[0, 0], [-1, -1]]