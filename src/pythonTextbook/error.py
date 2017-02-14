def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break


nums = [1, 2, 3]
for_func(nums, lambda i: print(i))

ages = {"taro": 20, "jiro": 15, "saburo": 18}
for_func(ages.items(), lambda i: print(i ))
