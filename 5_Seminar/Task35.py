# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

#    0  1  2  3  4  5  6
a = [1, 2, 3, 4, 6, 7, 8]

for i in range(1, len(a)):
    if a[i]-1 != a[i-1]:
        print(a[i]-1)
