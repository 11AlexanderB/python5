# task 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = input('Введите слова через пробел: ')
# print(text)
# new_text = ''
# for i in text.split():
#     if 'абв' not in i:
#         new_text += i + ' '
# print(new_text)


# task 2.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

symbols = input('Введите данные: ')
data = open('input_data.txt', 'w')
data.write(symbols)
data.close()

new_str = ''
i = 0

while i < len(symbols):
    count = 1
    while i+1 < len(symbols) and symbols[i] == symbols[i+1]:
        i += 1
        count += 1
    new_str += str(count) + symbols[i]
    i += 1

data = open('output.txt', 'w')
data.write(new_str)
data.close()








