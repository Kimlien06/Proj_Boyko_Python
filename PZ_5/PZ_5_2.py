# Описать функцию TrianglePS(параметры), вычисляющую по стороне a
# равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4. С
# помощью этой функции найти периметры и площади трех равносторонних
# треугольников с данными сторонами.

import math


def validate_input(a):
    while type(a) != float:
        try:
            a = float(a)
            if a <= 0:
                raise ValueError("Сторона треугольника должна быть положительным числом.")
            return a
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None


def triangle(a):
    p = 3 * a
    s = (a ** 2) * (math.sqrt(3) / 4)
    return p, s


def main():
    for i in range(1, 4):
        while True:
            a = input(f"Введите длину стороны {i}-го равностороннего треугольника: ")
            a = validate_input(a)
            if a is not None:
                break

        p, s = triangle(a)
        print(f"Для треугольника со стороной {a}:")
        print(f"Периметр P = {p}")
        print(f"Площадь S = {s:.6f}")
        print()


main()
