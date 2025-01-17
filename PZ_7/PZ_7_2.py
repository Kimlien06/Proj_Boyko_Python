# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
# символа строки, нарушающего алфавитный порядок.

input_string = input('Введите строку: ')
letters = []
result = 0

for sym in input_string:
    if sym.isalpha():
        letters.append(sym)

for i in range(len(letters) - 1):
    if ord(letters[i]) > ord(letters[i + 1]):
        result = i
        break

print(result)


