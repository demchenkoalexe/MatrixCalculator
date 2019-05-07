from MatrixRead import readFile

class MatrixCalculator():
	def __init__(self):
		pass

	## Метод, реализующий сложения двух матриц
	# @param A - матрица (двумерный список) первая
	# @param B - матрица (двумерный список) вторая
	# @return - матрица, результат сложения двух матриц
	def addTwoMatrix(self, A, B):
		C = [] #матрица результата
		#проверка матриц на соответсвие размерности
		if ( len(A) == len(B) and len(A[0]) == len(B[0]) ):
			for i in range(len(A) - 1):
				#проверка матриц на баги в строках (такие, как неодинаковое количество элементов)
				if ( len(A[i]) != len(A[i + 1]) or len(B[i]) != len(B[i + 1]) ):
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
			for i in range(len(A) - 1):
				#проверка матриц на баги в строках (такие, как неодинаковое количество элементов)
				if ( len(A[i]) != len(A[i + 1]) or len(B[i]) != len(B[i + 1]) ):
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
		for i in A:
			AnumberB = [] #одна строка будущей результирующей матрицы
			for j in i:
				AnumberB.append(j * B)
			C.append(AnumberB)
		return C


def main():
	mc = MatrixCalculator()

	operation, A, B = readFile('input.txt')

	C = []
	if ( operation == '+' ):
		C = mc.addTwoMatrix(A, B)
	elif ( operation == '-' ):
		C = mc.diffTwoMatrix(A, B)
	elif ( operation == '*' ):
		if ( type(B) == int ):
			C = mc.multiMatrixByNumber(A, B)

	if (C):
		print(C)
	else:
		print("You input non-corrective matrices. Check the dimemsions and rows of each matrix.")
	return

if __name__ == "__main__":
	main()