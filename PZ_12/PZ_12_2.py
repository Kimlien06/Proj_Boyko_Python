# Составить генератор (yield), который выводит из строки только цифры.

from string import digits


def only_number(string_test):
    digits_string = [char for char in string_test if char in digits]
    yield digits_string


string = input("Введите строку:")
new_digital_list = only_number(string)

for i in new_digital_list:
    print(i)
