# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин. Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bookmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
gallery = {'Чехов', 'Тютчев', 'Пушкин'}

all_book = magistr | domknigi | bookmarket | gallery
common_book = magistr & domknigi & bookmarket & gallery
not_all_book = all_book - common_book

print(all_book)
print(common_book)
print(not_all_book)
