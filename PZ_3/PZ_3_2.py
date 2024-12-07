# Размер скидки на продукты определен следующим образом: при покупке до 500 р.
# скидка составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при
# покупке от 1000 р. до 1500 р. скидка составит 4%; при покупке от 1500 р. до 2000 р.
# скидка составит 5%. Составить программу определяющую размер скидки в
# зависимости от потраченной суммы.

purchase_price = input('Введите стоимость покупки: ')
sale = 0

while type(purchase_price) != int:
    try:
        purchase_price = int(purchase_price)
        if purchase_price <= 0:
            raise ValueError('Стоимость покупки не может быть меньше 0')
    except ValueError:
        print("Неправильно введена сумма покупки")
        purchase_price = input('Введите стоимость покупки: ')

if purchase_price < 500:
    sale = 2
elif 500 <= purchase_price < 1000:
    sale = 3
elif 1000 <= purchase_price < 1500:
    sale = 4
elif 1500 <= purchase_price < 2000:
    sale = 5
else:
    sale = 0

print(f"Скидка на покупку продуктов составила {sale} %.")
