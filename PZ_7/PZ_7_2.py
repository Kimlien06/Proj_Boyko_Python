# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
# символа строки, нарушающего алфавитный порядок.

input_string = input('Введите строку: ')
letters = []

for sym in input_string:
    if sym.isalpha():
        letters.append(sym)

for i in range(1, len(letters)):
    if letters[i] < letters[i - 1]:
        for j in range(len(input_string)):
            if input_string[j] == letters[i]:
                print(j + 1)  # +1, так как индексация начинается с 0
                break
        break
else:
    print(0)

