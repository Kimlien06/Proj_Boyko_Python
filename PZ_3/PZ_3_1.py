# Дано целое число A. Проверить истинность высказывания: «Число A является четным».

A = input('Введите целое число: ')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели!')
        A = input('Введите целое число: ')

if A // 2 == 0:
    print("True")
else:
    print("False")
