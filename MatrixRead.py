import copy

def readFile(name):
	#ЧТЕНИЕ МАТРИЦ и ОПЕРАЦИИ НАД НИМИ ИЗ ФАЙЛА
	f = open(name, 'r')
	firstString = True
	matrixRead = []
	A = []
	for line in f:
		if (firstString):
			firstString = False
			operation = line[0]
			continue

		if (operation == '+' or operation == '-'):
			if (line == '\n'):
				if (not A):
					A = copy.copy(matrixRead)
					matrixRead = []
			else: 
				m = line.rstrip().split(' ')
				m = [int(item) for item in m]
				matrixRead.append(m)
	
	B = copy.copy(matrixRead)
	f.close()
	return operation, A, B