def func(num):
    mylist = [num]
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
            mylist.append(num)
        else:
            num = num // 2
            mylist.append(num)
    return mylist, len(mylist) - 1


num = int(input('请输入一个数组：'))
print(func(num))
