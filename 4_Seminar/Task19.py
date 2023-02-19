#19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime
n = int(input())
rand = datetime.datetime.now().microsecond%(n+1)
print(rand)