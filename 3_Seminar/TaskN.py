start_lst = [1.1, 1.2, 3.1, 5, 10.01]
next_list = []

for i in start_lst:
    next_list.append(round(i % 1, 3))
print(next_list)

max = next_list[0]
min = next_list[0]

for i in next_list:
    if i != 0 and i > max:
        max = i
    if i != 0 and i < min:
        min = i

print(max - min)

k = int(input('Введите число: '))

lst_fib = []

# FIBONACCI
# Для положительных
a = 1
b = 1
for i in range(k):
    lst_fib.append(a) # Первым действие вставляем значение "а" в список, а затем выщитываем новое значение "а"
    temp = a  # храним значение "a" во временной переменной
    a = b  # значение "a" уже в списке, поэтому приравниваем новое значение, равное "b"
    b = temp + a  # следующее значение равно сумме прошлого и текущего значения "a"

#Для отрицательных
a = 0
b = 1
for i in range(k+1):
    lst_fib.insert(0, a) # Каждый раз вставляем значение "a" на позицию с индексом 0
    temp = a
    a = b
    b = temp - a

print(lst_fib)
