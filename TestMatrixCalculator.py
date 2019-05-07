import unittest
from MatrixCalculator import *

class TestMatrixCalculator(unittest.TestCase):

	def test_matrixCalcCreationTest(self):
		mc = MatrixCalculator()
		self.assertIsNotNone(mc)

	def test_add(self):
		mc = MatrixCalculator()
		A = [[1, 1], [2, 2]]
		B = [[1, 1], [3, 3]]
		C = [[2, 2], [5, 5]]
		self.assertEquals(mc.addTwoMatrix(A, B), C) #при сложении матриц A и B, получим C

		D = [[1, 1, 1], [2, 2, 2]]
		self.assertFalse(mc.addTwoMatrix(A, D)) #ошибка при попытке сложить матрицы разной размерности

	def test_diff(self):
		mc = MatrixCalculator()
		A = [[2, 2], [1, 1]]
		B = [[1, 1], [3, 3]]
		C = [[1, 1], [-2, -2]]
		self.assertEquals(mc.diffTwoMatrix(A, B), C) #при разности матриц A и B, получим C

		D = [[1, 1, 1], [2, 2, 2]]
		self.assertFalse(mc.diffTwoMatrix(A, D)) #ошибка при попытке вычесть матрицы разной размерности

	def test_multiByNumber(self):
		mc = MatrixCalculator()
		A = [[2, 2, 2, 2], [3, 4, 5, 6]]
		num1 = 0
		self.assertEquals(mc.multiMatrixByNumber(A, num1), [[0, 0, 0, 0], [0, 0, 0, 0]])

		num2 = 4
		self.assertEquals(mc.multiMatrixByNumber(A, num2), [[8, 8, 8, 8], [12, 16, 20, 24]])



if __name__ == "__main__":
	unittest.main()