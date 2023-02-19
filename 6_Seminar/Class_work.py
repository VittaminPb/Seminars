# lambda, filter, map, zip, enumerate, list comprehension

# list comprehension:

# можно использовать разные действия вместо i -> [i*i for i in range(1, 10)]
a = [i for i in range(1, 10)]
print(a)

# -------- раньше писали так: ----------
a = []
for i in range(1, 10):
    a.append(i)
print(a)


# enumerate:

a = [2, 4, 6, 8]
for indx, val in enumerate(a):
    print(indx, val)  # печать индекса и элемента списка

    # -------- раньше писали так: ----------
a = [2, 4, 6, 8]
for i in range(len(a)):
    print(i)  # печать индекса списка


# zip

a = [1, 2, 3, 4, 5, 6]
months = ["jan", "feb", "mar", "apr", "may"]

result = list(zip(a, months))  # объединение элементов 1 и 2 списков в кортежи
print(result)
print(result[2][1])  # вывести на печать элемент кортежа 2, позиция 1


# lambda

sum = lambda a, b: a+b # sum = lambda a, b: a+b if a>5 else 0 # вывод a+b усли a>5 иначе выдаст 0
print(sum(2, 3))

# -------- раньше писали так: ----------
def sum(a, b):
    return a+b

print(sum(2, 3))  # вывод на печать результата работы функции sum с паременными 2 и 3


## map

a = [2, 4, 6, 8]
a = list(map(lambda x: x*x, a)) 
print(a)


## filter

a = [1, 2, 3, 4, 5, 6, 8, 9, 0]
def sorting(x):
    if x%2==0:
        return True
res = list(filter(sorting, a)) # отфильтровывает список по параметрам функции sorting и составляет новый список res.
print(res)

# либо через lambda:
res = list(filter(lambda x: not x%2, a))
print(res)


## sorted

a = [(6,5,5), (4,5,5), (1,2,3)]

res = sorted(a, key = lambda x: (x[2], x[1], x[0])) # отсортировывает список по третьему элементу кортежа. Если они равны, то по 2-му, если равны, то по первому.
print(res)
res = sorted(a, key = lambda x: (x[2], x[1], x[0]), reverse=True) # наоборот, от бОльшего к меньшему
print(res)