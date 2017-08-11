import math


def F(n):
    mother = 0
    for i in range(1, n + 1):
        mother += 0.9 ** i

    child = 0
    for i in range(1, n + 1):
        child += 0.81 ** i
    child = math.sqrt(child)

    return child / mother


def f(n):
    sum_geometric_progression = math.sqrt(0.81 / 0.19) / 9
    return (F(n) - sum_geometric_progression) / (F(1) - sum_geometric_progression) * 1200


def g(X):
    return 2.0 ** (X / 800)


def g_inverse(X):
    return 800 * math.log(X, 2)


if __name__ == '__main__':
    N = int(input())
    RPerf = []
    for i in range(N):
        RPerf.append(int(input()))

    arg_mother = 0
    for i in range(1, N + 1):
        arg_mother += 0.9 ** i

    arg_child = 0
    for i in range(1, N + 1):
        arg_child += g(RPerf[i - 1]) * (0.9 ** i)
    ans = g_inverse(arg_child / arg_mother) - f(N)
    print(int(ans))
