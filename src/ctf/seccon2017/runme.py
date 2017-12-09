import sys

sys.setrecursionlimit(99999)


def f(n):
    return n if n < 2 else f(n - 2) + f(n - 1)


tmp1 = 1
tmp2 = 1
for i in range(11009):
    tmp = tmp2
    tmp2 = tmp1 + tmp
    tmp1 = tmp

print("SECCON{" + str(tmp2)[:32] + "}")

# print("SECCON{" + str(f(11011))[:32] + "}")
