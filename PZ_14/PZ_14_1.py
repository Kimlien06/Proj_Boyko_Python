# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re

with open('hotline.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

valid_lines = []
invalid_lines = []

processed_lines = map(lambda line: (
    line,
    re.search(r'- (\d[\d\s]*\d)$', line.strip())
), lines)

for line, phone_match in processed_lines:
    (valid_lines if phone_match and len(re.sub(r'\D', '', phone_match.group(1))) == 11
     else invalid_lines).append(line)

with open('valid_phones.txt', 'w', encoding='utf-8') as file:
    file.writelines(valid_lines)

with open('invalid_phones.txt', 'w', encoding='utf-8') as file:
    file.writelines(invalid_lines)

print(f"Количество строк с корректными номерами: {len(valid_lines)}")
print(f"Количество строк с некорректными номерами: {len(invalid_lines)}")
