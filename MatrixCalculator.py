from MatrixRead import readFile, getEMatrix
import copy

class MatrixCalculator():
	def __init__(self):
		pass

	## Метод, реализующий провекру ошибки ввода матрицы
	# @param A - матрица (двумерный список) первая
	# @return - True or False
	@staticmethod
	def bagMatrix(A):
		for i in range(len(A) - 1):
			#проверка матрицы на баги в строках (такие, как неодинаковое количество элементов)
			if ( len(A[i]) != len(A[i + 1])):
				return True
		return False

	## Метод, реализующий сложения двух матриц
	# @param A - матрица (двумерный список) первая
	# @param B - матрица (двумерный список) вторая
	# @return - матрица, результат сложения двух матриц
	def addTwoMatrix(self, A, B):
		C = [] #матрица результата
		#проверка матриц на соответсвие размерности
		if ( len(A) == len(B) and len(A[0]) == len(B[0]) ):
			if (MatrixCalculator.bagMatrix(A) and MatrixCalculator.bagMatrix(B)):
				return False

			#непосредственно сложение
			for i in range(len(A)):
				AplusB = [] #одна строка будущей результирующей матрицы
				for j in range(len(A[i])):
					AplusB.append(A[i][j] + B[i][j])
				C.append(AplusB)
		else:
			return False
		return C

	## Метод, реализующий разность двух матриц
	# @param A - матрица (двумерный список) первая
	# @param B - матрица (двумерный список) вторая
	# @return - матрица, результат разности двух матриц
	def diffTwoMatrix(self, A, B):
		C = [] #матрица результата
		#проверка матриц на соответсвие размерности
		if ( len(A) == len(B) and len(A[0]) == len(B[0]) ):
			if (MatrixCalculator.bagMatrix(A) and MatrixCalculator.bagMatrix(B)):
				return False

			#непосредственно разность
			for i in range(len(A)):
				AminusB = [] #одна строка будущей результирующей матрицы
				for j in range(len(A[i])):
					AminusB.append(A[i][j] - B[i][j])
				C.append(AminusB)
		else:
			return False
		return C

	## Метод, реализующий умножение матрицы на число
	# @param A - матрица (двумерный список)
	# @param B - число
	# @return - матрица, результат умножения матрицы на число
	def multiMatrixByNumber(self, A, B):
		C = [] #матрица результата
		if (MatrixCalculator.bagMatrix(A)):
			return False
		for i in A:
			AnumberB = [] #одна строка будущей результирующей матрицы
			for j in i:
				AnumberB.append(j * B)
			C.append(AnumberB)
		return C

	## Метод, реализующий транспонирование матрицы
	# @param A - матрица (двумерный список)
	# @return - матрица, результат транспонирования
	def transpose(self, A):
		C = [] #матрица результата
		if (MatrixCalculator.bagMatrix(A)):
			return False
		for i in range(len(A[0])):
			Atranspose = []
			for j in range(len(A)):
				Atranspose.append(A[j][i])
			C.append(Atranspose)
		return C

	## Метод, реализующий произведение матриц
	# @param A - матрица (двумерный список) первая NxM
	# @param B - матрица (двумерный список) вторая MxK
	# @return - матрица, результат произведения
	def multiTwoMatrix(self, A, B):
		C = [] #матрица результата
		#проверка матриц на соответсвие размерности
		if ( len(A[0]) == len(B) ):
			if (MatrixCalculator.bagMatrix(A) and MatrixCalculator.bagMatrix(B)):
				return False
			Bt = self.transpose(B)
			for i in A:
				AmultiB = []
				for j in Bt:
					c = 0
					for k in range(len(i)):
						c += i[k] * j[k]
					AmultiB.append(c)
				C.append(AmultiB)
		else:
			return False
		return C

	## Метод, реализующий возведение матрицы в степень
	# @param A - матрица (двумерный список) NxN
	# @param B - степень
	# @return - матрица, результат возведения в степень
	def powMatrix(self, A, B):
		C = copy.copy(A) #матрица результата
		#проверка матриц на соответсвие размерности
		if ( len(A[0]) == len(A) ):
			if (MatrixCalculator.bagMatrix(A)):
				return False
			if ( B == 1 ):
				return C
			elif( B == 0 ):
				C = getEMatrix(len(A))
				return C
			else:
				i = 0
				while ( i < B - 1 ):
					C = copy.copy(self.multiTwoMatrix(C, A))
					i += 1
		else:
			return False
		return C


def main():
	mc = MatrixCalculator()

	operation, A, B = readFile('input.txt')
	if (not operation):
		return

	print(operation, A, B)

	C = []
	if ( operation == '+' ):
		C = mc.addTwoMatrix(A, B)
	elif ( operation == '-' ):
		C = mc.diffTwoMatrix(A, B)
	elif ( operation == '*' ):
		if ( type(B) == int ):
			C = mc.multiMatrixByNumber(A, B)
		else:
			C = mc.multiTwoMatrix(A, B)
	elif ( operation == 'T' ):
		C = mc.transpose(A)
	elif ( operation == '^' ):
		if (B < 0):
			print("Negative degree. Correct.")
			return
		C = mc.powMatrix(A, B)

	if (C):
		print(C)
	else:
		print("You input non-corrective matrices. Check the dimemsions and rows of each matrix.")
	return

if __name__ == "__main__":
	main()