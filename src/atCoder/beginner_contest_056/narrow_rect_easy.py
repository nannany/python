inputs = input().split()
W = int(inputs[0])
a = int(inputs[1])
b = int(inputs[2])

if abs(a - b) <= W:
    print(0)
else:
    print(abs(a - b) - W)
