"""
Додаткові завдання по матрицях (надіслати як завжди мені в лс після виконання основного дз):
створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
вивести на екран
- вивести суму чисел головної діагоналі матриці
- вивести мінімальне та максимальне значення побічної діагоналі матриці
- ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
- ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
"""
from random import randint
import copy

matrix = [[randint(10, 99) for _ in range(10)] for _ in range(10)]
new_column_matrix = copy.deepcopy(matrix)
new_row_matrix = copy.deepcopy(matrix)

for row in matrix:
    for number in row:
        print(number, end=' ')
    print()

main_diagonal_matrix_sum = 0

# перебираем вложеные списки в списке от 0 до 10
for i in range(len(matrix)):
    # добавляем значение диагонали и суммируем
    main_diagonal_matrix_sum += matrix[i][i]
print(f'сумма чисел главной диагонали матрицы: {main_diagonal_matrix_sum}')

else_diagonal_matrix_sum = 0
else_diagonal_matrix = []

for i in range(len(matrix)):
    else_diagonal_matrix.append(matrix[i][len(matrix) - 1 - i])
print(
    f'максимальное и минимальное значение побочной диагонали: {max(else_diagonal_matrix)}, {min(else_diagonal_matrix)}')

select_column = int(input("введите номер столбика: "))
for row in matrix:
    print(row[select_column - 1], end=' ')

print("\n")
select_row = int(input("введите номер строки: "))
print(matrix[select_row - 1])

print('\n')

select_first_column = int(input("введите номер столбика: "))
select_second_column = int(input('введите номер столбика для замены: '))

if 1 <= select_first_column <= 10 and 1 <= select_second_column <= 10:
    for row in new_column_matrix:
        row[select_first_column - 1], row[select_second_column - 1] = row[select_second_column - 1], row[select_first_column-1]
        for number in row:
            print(number, end=' ')
        print()
else:
    print("такого столбца не существует")

print("\n")

select_first_row = int(input("введите номер строки: "))
select_second_row = int(input("введите номер строки для замены: "))

if 1 <= select_first_row <= 10 and 1 <= select_second_row <= 10:
    new_row_matrix[select_first_row - 1], new_row_matrix[select_second_row-1] = new_row_matrix[select_second_row - 1], new_row_matrix[select_first_row-1]
    for row in new_row_matrix:
        for number in row:
            print(number, end=' ')
        print()
else:
    print("такой строки не существует")
