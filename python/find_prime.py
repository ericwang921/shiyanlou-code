def find_prime(num):
    if num > 1:  # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print('is not prime number')
                print(i, '*', num // i, '=', num)
                break
        else:
            print('is prime number')
    else:
        print('is not prime number')


num = int(input('please input a number:'))
find_prime(num)
