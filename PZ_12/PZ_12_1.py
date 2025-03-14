# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

import random
N = int(input("Введите количество чисел в списке:"))
main_list = []
for _ in range(1, N+1):
    main_list.append(random.randint(1, 100))
print(main_list)

first_list = [x for x in main_list if x % 3 == 0]
print(f'Числа, которые деляться на 3: {first_list}')

second_list = [x for x in main_list if not (x % 3 == 0)]
print(f'Числа, которые не деляться на 3: {second_list}')

print(f'{len(first_list)}')
print(len(second_list))

