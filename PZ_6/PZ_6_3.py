# Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.

def swap_pairs(lst):
    if len(lst) % 2 != 0:
        raise ValueError("Список должен иметь четное количество элементов.")

    for i in range(0, len(lst), 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst



def main():
    try:
        n = int(input("Введите четное число N (размер списка): "))
        if n <= 0:
            print("Размер списка должен быть положительным числом.")
            return
        if n % 2 != 0:
            print("N должно быть четным числом.")
            return

        print(f"Введите {n} элементов списка через пробел:")
        lst = list(map(int, input().split()))

        if len(lst) != n:
            print(f"Ожидалось {n} элементов, но введено {len(lst)}.")
            return

        result = swap_pairs(lst)
        print("Список после обмена элементов попарно:", result)

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


main()
