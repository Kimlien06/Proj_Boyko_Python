# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг
# конфет.

sweet_prise = float(input("Введите цену 1 кг конфет: "))
amount_sweet = 1
cost_sweet = 0

while type(sweet_prise) != float:
    try:
        sweet_prise = float(sweet_prise)
    except ValueError:
        print("Неккоретно введены данные")
        sweet_prise = float(input("Введите цену 1 кг конфет: "))

while amount_sweet != 10:
    cost_sweet = sweet_prise * amount_sweet
    amount_sweet += 1
    print(cost_sweet, end="  ")


