data = [i * 2 for i in range(1, 6)]
print(data)

data2 = [i * 2 - 1 for i in range(1, 6)]
print(data2)

data3 = [i for i in range(1, 11) if i % 2 == 1]
print(data3)

base = [1, 2, 3]
result = [(x, y) for x in base for y in base if x != y]
print(result)

res = ["fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(1, 21)]
print(res)
