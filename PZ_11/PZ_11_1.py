# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

list_num = ['4 7 -47 -6 90 -34 24']
f1 = open('test_1.txt', 'w')
f1.writelines(list_num)
f1.close()


f2 = open('test_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(list_num)
f2.close()


f1 = open('test_1.txt')
line = f1.read()
line = line.split()
f1.close()

f1 = open('test_1.txt')
min_num, sq_num, sum_sq_num, arg_sum_sq_num = 0, [], 0, 0
for i in range(len(line)):
    min_num = min_num if min_num < int(line[i]) else int(line[i])
    if int(line[i]) % 2 == 0:
        sq_num.append(int(line[i]) ** 2)
for i in range(len(sq_num)):
    sum_sq_num += sq_num[i]
    arg_sum_sq_num = sum_sq_num / len(sq_num)
f1.close()


f2 = open('test_2.txt', 'a')
f2.write('\n')
f2.write(f'Количество элементов:, {len(line)}')
f2.write('\n')
f2.write(f'Минимальный элемент: {min_num}')
f2.write('\n')
f2.write(f'Квадраты четных элементов: {sq_num}')
f2.write('\n')
f2.write(f'Сумма квадратов четных элементов: {sum_sq_num}')
f2.write('\n')
f2.write(f'Среднее арифметическое суммы квадратов четных элементов: {arg_sum_sq_num}')
f2.close()
