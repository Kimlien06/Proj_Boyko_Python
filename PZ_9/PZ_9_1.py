# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

products = {}
inf = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
inf = inf.split()

products['Продукт 1'] = inf[0]
products['Продажи по дням апельсинов'] = []
for i in inf[1:6]:
    products['Продажи по дням апельсинов'].append(int(i))

products['Продукт 2'] = inf[6]
products['Продажи по дням яблок'] = []
for i in inf[7:]:
    products['Продажи по дням яблок'].append(int(i))

print(products)
print(f"Максимальная продажа апельсинов составляет {max(products['Продажи по дням апельсинов'])} кг")
print(f"Максимальная продажа яблок составляет {max(products['Продажи по дням яблок'])} кг")

