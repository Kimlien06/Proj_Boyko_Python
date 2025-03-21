# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

size = int(input("Введите размер массива: "))
matrix = [[i + j * size for i in range(size)] for j in range(size)]


print("Исходная матрица:")
for row in matrix:
    print(row)


matrix = [
    [element * 2 if i == j else element for j, element in enumerate(row)]
    for i, row in enumerate(matrix)
]


print("\nМатрица после изменения:")
for row in matrix:
    print(row)
