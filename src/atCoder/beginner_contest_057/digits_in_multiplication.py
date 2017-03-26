import math

N = int(input())

for i in range(1, math.ceil(math.sqrt(N)) + 1):
    if N % i == 0:
        factor1 = N / i
        factor2 = i

factor1 = int(factor1)

if factor1 < factor2:
    print(len(str(factor2)))
else:
    print(len(str(factor1)))
