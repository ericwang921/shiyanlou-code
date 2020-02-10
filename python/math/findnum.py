def find_max(nums):
    max_n = nums[0]
    for x in nums:
        if x > max_n:
            max_n = x
    return max_n


def find_min(nums):
    min_n = nums[0]
    for x in nums:
        if x < min_n:
            min_n = x
    return min_n


def main():
    nums = [41, 67, 2, 3, 45, 6, 7, 8, 9, 55, 3, 2, 123]
    print('max:', find_max(nums))
    print(f'min: {find_min(nums)}')


if __name__ == '__main__':
    main()
