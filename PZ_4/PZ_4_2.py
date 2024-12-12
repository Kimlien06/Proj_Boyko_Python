# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
# вывести TRUE, если нет — вывести FALSE.

N = input("Введите целое число: ")
flag = False
while type(N) != int:
    try:
        N = int(N)
        if N < 0:
            raise ValueError("Число не может быть меньше 0")
    except ValueError:
        print("Неккоретно введены данные")
        N = int(input("Введите целое число: "))

while True:
    digit = N % 10

    if digit == 2:
        flag = True
        break

    N = N // 10

print(flag)
