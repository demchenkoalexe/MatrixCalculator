import copy

def readFile(name):
	#ЧТЕНИЕ МАТРИЦ и ОПЕРАЦИЙ НАД НИМИ ИЗ ФАЙЛА
	f = open(name, 'r')
	firstString = True
	matrixRead = []
	A, B = [], []
	for line in f:
		if (firstString):
			firstString = False

			m = line.rstrip().split(' ')
			operation = m[0]

			if (operation == '*' or operation == '^'):  #в случае умножения на число или возведения в степень
				if ( len(m) > 1 ):
					B = int(m[1])
				elif (operation == '^'):
					print('Input power.')
					return None, None, None
			continue

		if (operation):
			if (line == '\n'):
				if (not A):
					A = copy.copy(matrixRead)
					matrixRead = []
				if (B or B == 0):
					return operation, A, B
				elif (operation == 'T'):
					return operation, A, None
			else: 
				m = line.rstrip().split(' ')
				m = [int(item) for item in m]
				matrixRead.append(m)
	
	B = copy.copy(matrixRead)
	f.close()
	return operation, A, B

#получить квадратная единичную матрицу размерности NxN
def getEMatrix(n):
	i = 0
	C = []
	while ( i < n ):
		c = [0 for i in range(n)]
		c[i] = 1
		C.append(c)
		i += 1
	return C