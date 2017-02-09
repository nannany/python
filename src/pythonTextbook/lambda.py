# coding:utf-8
nums = [1, 3, 4, 4, 6]
# map
print(list(map(lambda a: a + 3, nums)))
print(list(map(lambda a: a * 3, nums)))
print(list(map(lambda a: a // 3, nums)))
# filter
print(list(filter(lambda x: (x % 2) == 0, nums)))
print(list(filter(lambda x: (x % 2) == 1, nums)))
# iter
i = iter(nums)
print(next(i))
print(next(i))
print(next(i))
