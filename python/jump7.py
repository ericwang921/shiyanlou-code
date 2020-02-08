# -*- coding: UTF-8 -*-

l1 = range(1, 101)

for a in l1:
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    else:
        print(a, end=" ")
