# Размер скидки на продукты определен следующим образом: при покупке до 500 р.
# скидка составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при
# покупке от 1000 р. до 1500 р. скидка составит 4%; при покупке от 1500 р. до 2000 р.
# скидка составит 5%. Составить программу определяющую размер скидки в
# зависимости от потраченной суммы.

purchase_price = input('Введите стоимость покупки: ')
sale = 100

while type(purchase_price) != int:
    try:
        purchase_price = int(purchase_price)
        if purchase_price <= 0:
            raise ValueError('Стоимость покупки не может быть меньше 0')
    except ValueError:
        print("Неправильно введена сумма покупки")
        purchase_price = input('Введите стоимость покупки: ')

if purchase_price < 500:
    sale -= 98
    purchase_price = purchase_price * 0.98
elif 500 <= purchase_price < 1000:
    sale -= 97
    purchase_price = purchase_price * 0.97
elif 1000 <= purchase_price < 1500:
    sale -= 96
    purchase_price = purchase_price * 0.96
elif 1500 <= purchase_price < 2000:
    sale -= 95
    purchase_price = purchase_price * 0.95
else:
    sale -= 100

print(f"Скидка на покупку продуктов составила {sale} %.")

