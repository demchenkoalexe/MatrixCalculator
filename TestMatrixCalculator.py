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
		self.assertEqual(mc.addTwoMatrix(A, B), C) #при сложении матриц A и B, получим C

		D = [[1, 1, 1], [2, 2, 2]]
		self.assertFalse(mc.addTwoMatrix(A, D)) #ошибка при попытке сложить матрицы разной размерности

	def test_diff(self):
		mc = MatrixCalculator()
		A = [[2, 2], [1, 1]]
		B = [[1, 1], [3, 3]]
		C = [[1, 1], [-2, -2]]
		self.assertEqual(mc.diffTwoMatrix(A, B), C) #при разности матриц A и B, получим C

		D = [[1, 1, 1], [2, 2, 2]]
		self.assertFalse(mc.diffTwoMatrix(A, D)) #ошибка при попытке вычесть матрицы разной размерности

	def test_multiByNumber(self):
		mc = MatrixCalculator()
		A = [[2, 2, 2, 2], [3, 4, 5, 6]]
		num1 = 0
		self.assertEqual(mc.multiMatrixByNumber(A, num1), [[0, 0, 0, 0], [0, 0, 0, 0]])

		num2 = 4
		self.assertEqual(mc.multiMatrixByNumber(A, num2), [[8, 8, 8, 8], [12, 16, 20, 24]])

	def test_transpose(self):
		mc = MatrixCalculator()
		A = [[2, 3, 4, 5], [9, 8, 2, 5]]
		self.assertEqual(mc.transpose(A), [[2, 9], [3, 8], [4, 2], [5, 5]])

	def test_multi(self):
		mc = MatrixCalculator()
		A = [[-1, 2, -3, 0], [5, 4, -2, 1], [-8, 11, -10, -5]]
		B = [[-9, 3], [6, 20], [7, 0], [12, -4]]
		C = [[0, 37], [-23, 91], [8, 216]]
		self.assertEqual(mc.multiTwoMatrix(A, B), C)

		D = [[1, 1], [2, 2]]
		self.assertFalse(mc.multiTwoMatrix(A, D))

	def test_pow(self):
		mc = MatrixCalculator()
		A = [[1, 2], [3, 4]]
		pow1 = 0
		pow2 = 4
		self.assertEqual(mc.powMatrix(A, pow1), [[1, 0], [0, 1]])
		self.assertEqual(mc.powMatrix(A, pow2), [[199, 290], [435, 634]])

		D = [[1], [1, 2]]
		self.assertFalse(mc.powMatrix(D, pow2))

if __name__ == "__main__":
	unittest.main()