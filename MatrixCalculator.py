from MatrixRead import readFile

class MatrixCalculator():
	def __init__(self):
		pass

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

def main():
	mc = MatrixCalculator()

	operation, A, B = readFile('input.txt')

	if ( operation == '+' ):
		C = mc.addTwoMatrix(A, B)
		print(C)

if __name__ == "__main__":
	main()