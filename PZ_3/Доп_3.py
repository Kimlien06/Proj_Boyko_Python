# Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
# в противном случае уменьшить на 2.

a = int(input('Введите двузначное число: '))
first_number = a / 10
second_number = a % 10

if (first_number + second_number) // 2 == 0:
    a *= 2
else:
    a /= 2

print(a)