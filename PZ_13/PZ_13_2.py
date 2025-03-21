# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

from functools import reduce

# Пример матрицы
matrix = [
    [1, -2, 3],
    [4, 5, 6],
    [7, 8, -10]
]


def is_positive_even(element):
    return element > 0 and element % 2 == 0


positive_even_elements = [element for row in matrix for element in row if is_positive_even(element)]


print("Массив положительных чётных элементов:", positive_even_elements)

if positive_even_elements:
    sum_elements = reduce(lambda x, y: x + y, positive_even_elements)
    average = sum_elements / len(positive_even_elements)
    print(f"Сумма элементов: {sum_elements}")
    print(f"Среднее арифметическое: {average}")
else:
    print("В матрице нет положительных чётных элементов.")
