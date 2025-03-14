# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

with open('text18-3.txt', 'r', encoding='utf-16') as file:
    lines = file.readlines()


print("Содержимое файла:")
for line in lines:
    print(line.strip())


punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


punctuation_count = 0
for line in lines[:4]:
    for char in line:
        if char in punctuation:
            punctuation_count += 1

print(f"\nКоличество знаков пунктуации в первых четырех строках: {punctuation_count}")


third_line = lines[2]
third_line_codes = ' '.join(str(ord(char)) for char in third_line)


with open('output_poem.txt', 'w', encoding='utf-16') as output_file:
    for i, line in enumerate(lines):
        if i == 2:
            output_file.write(third_line_codes + '\n')
        else:
            output_file.write(line)
