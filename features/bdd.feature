Feature: Matrix Calculator testing

  Scenario: Add two matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first matrix
    And we have [[1, 1], [3, 3]] as second matrix
    Then the add result should be [[2, 2], [5, 5]]

  Scenario: Diff two matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first matrix
    And we have [[1, 1], [3, 3]] as second matrix
    Then the diff result should be [[0, 0], [-1, -1]]

  Scenario: Multi matrix by number matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first matrix
    And we have 2 number
    Then the multi matrix by number result should be [[2, 2], [4, 4]]

  Scenario: Transpose matrix
    Given we have matrix calculator
    When we have [[1, 1], [2, 2]] as first matrix
    Then the transpose result should be [[1, 2], [1, 2]]

  Scenario: Multi two matrix
    Given we have matrix calculator
    When we have [[-1, 2, -3, 0], [5, 4, -2, 1], [-8, 11, -10, -5]] as first matrix
    And we have [[-9, 3], [6, 20], [7, 0], [12, -4]] as second matrix
    Then the multi result should be [[0, 37], [-23, 91], [8, 216]]