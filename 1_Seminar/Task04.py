# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

n = float(input("Введите десятичную дробь: "))

res = int(n*10 % 10)

if res == 0:
    print("нет")
else:
    print(res)

# Второй способ:

n = input()
a = n.split('.')
print(a[1][0])
