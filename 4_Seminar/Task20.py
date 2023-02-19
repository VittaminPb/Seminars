# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

a = ["st", "qwe", "12", "tyy"]
for i in a:
    if i.isdigit():
        print(a.index(i))
        
# or

a = ["st", "qwe", 12, "tyy"]
for i in a:
    if type(i) == int:
        print(a.index(i))
