# Составить функцию, которая выполнит суммирования числового ряда.
def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return None  # Завершение ввода
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")


def input_and_sum_series():
    print("Введите числа для числового ряда (введите 'q' для завершения ввода):")
    total_sum = 0
    while True:
        number = get_numeric_input("Введите число: ")
        if number is None:
            break  # Завершение ввода
        total_sum += number
    return total_sum


def main():
    total_sum = input_and_sum_series()
    if total_sum == 0:
        print("Ввод завершен. Нет чисел для суммирования.")
    else:
        print(f"Сумма числового ряда равна: {total_sum}")


main()
