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

			if (operation == '*'):  #в случае умножения на число
				if ( m[1] ):
					B = int(m[1])
			continue

		if (operation):
			if (line == '\n'):
				if (not A):
					A = copy.copy(matrixRead)
					matrixRead = []
				if (B):
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