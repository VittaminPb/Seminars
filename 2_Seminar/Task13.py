# 13. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

one = input()
two = input()
count = 0
for i in range(len(one)-len(two)+1):
    if one[i:i+len(two)] == two:
        count+=1
print(count)

# второй способ:
one = input()
two = input()
print(one.count(two))