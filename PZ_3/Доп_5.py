# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

a, b = int(input('Введите первое число: ')), int(input('Введите первое число: '))
n = a + b

if n // 5:
    n += 1
else:
    n -= 2

print(n)
