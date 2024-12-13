# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

def find_first_local_minimum(lst):
    if not lst:
        return None

    for i in range(len(lst)):
        if i == 0 and len(lst) > 1 and lst[i] < lst[i + 1]:
            return i
        elif i == len(lst) - 1 and len(lst) > 1 and lst[i] < lst[i - 1]:
            return i
        elif 0 < i < len(lst) - 1 and lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            return i

    return None


def main():
    try:
        N = int(input("Введите размер списка N: "))
        if N <= 0:
            print("Размер списка должен быть положительным числом.")
            return

        print(f"Введите {N} элементов списка через пробел:")
        lst = list(map(int, input().split()))

        if len(lst) != N:
            print(f"Ожидалось {N} элементов, но введено {len(lst)}.")
            return

        result = find_first_local_minimum(lst)
        if result is not None:
            print(f"Номер первого локального минимума: {result}")
        else:
            print("Локальный минимум не найден.")

    except ValueError:
        print("Ошибка: введите корректные числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


main()
