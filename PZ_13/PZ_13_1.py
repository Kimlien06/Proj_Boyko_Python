# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


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
