# КАЛЬКУЛЯТОР МАТРИЦ

Для успешной работы в файле 'input.txt', созданного рядом с 'MatrixCalculator.py', нужно ввести:

## 1. Для сложения матриц: 

Первая строчка: +.

Вторая и последующие строчки: матрицы А и В, каждая строка матрицы в отдельной строке файла, между элементами строки пробел, между матрицами перенос строки ('\n'). Элементы матрицы только числа. 

Например, 

```
+
1 1
2 2

1 1
3 3
```

ВАЖНО! Складывать можно только матрицы одинаковой размерности.

## 2. Для разности:

Первая строчка: -. 

Ввод матриц как и со сложением.

## 3. Для умножения матрицы на число: 

Первая строчка: * и (число).

Вторая и последующая строчки: матрица А, каждая строка матрицы в отдельной строке файла, между элементами строки пробел. Если матрица будет в файле две, считается только одна первая.

Например, 
```
* 12
1 2 2 3
9 0 9 3
0 0 0 7
```

## 4. Для тарнспонирования: 
Первая строчка: T (англ. прописная).

Вторая и последующая строчки: матрица А, каждая строка матрицы в отдельной строке файла, между элементами строки пробел. Если матрица будет в файле две, считается только одна первая.

Например, 
```
T
1 2 2 3
9 0 9 3
0 0 0 7
```