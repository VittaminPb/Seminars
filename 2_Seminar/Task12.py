# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

#     *Пример:*

#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
dictionary = {}

for i in range(1, n+1):
    dictionary[i] = i*3+1
print(dictionary)
