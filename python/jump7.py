list = range(1, 101)

for a in list:
    if a % 7 == 0 or a % 10 == 7 or a//10 == 7:
        continue
    else:
        print(a, end=" ")
