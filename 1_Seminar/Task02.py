# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите число: '))
max_num = a
for i in range(4):
    a = int(input('Введите число: '))
    if max_num < a:
        max_num = a
print(max_num)

# 2 метод

list = []
for i in range(0, len(list)):
    i = list.append(int(input("Введите число:")))
max = list[0]
for i in list:
    if max < i:
        max = i
print(max)
