import unittest
from MatrixCalculator import MatrixCalculator as mc

class TestMatrixCalculator(unittest.TestCase):

	def matrixCalcCreationTest(self):
		self.matrixCalculator = mc.MatrixCalculator()
		self.assertIsNotNone(self.matrixCalculator)

if __name__ == "__main__":
	unittest.main()