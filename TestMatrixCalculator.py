import unittest
from MatrixCalculator import *

class TestMatrixCalculator(unittest.TestCase):

	def test_matrixCalcCreationTest(self):
		matrixCalculator = MatrixCalculator()
		self.assertIsNotNone(matrixCalculator)

if __name__ == "__main__":
	unittest.main()