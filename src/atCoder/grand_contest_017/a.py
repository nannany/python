import math

if __name__ == '__main__':
    N, P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    zero_or_one = [(i % 2) for i in A]

    count_zero = zero_or_one.count(0)
    count_one = zero_or_one.count(1)

    if P == 0:
        sum_combination_zero = 0
        for i in range(0, count_zero + 1):
            sum_combination_zero += math.factorial(count_zero) / (math.factorial(i) * math.factorial(count_zero - i))

        sum_combination_one = 0
        for i in range(0, count_one + 1, 2):
            sum_combination_one += math.factorial(count_one) / (math.factorial(i) * math.factorial(count_one - i))

        ans = sum_combination_zero * sum_combination_one
        print(int(ans))
    else:
        sum_combination_zero = 0
        for i in range(0, count_zero + 1):
            sum_combination_zero += math.factorial(count_zero) / (math.factorial(i) * math.factorial(count_zero - i))

        sum_combination_one = 0
        for i in range(1, count_one + 1, 2):
            sum_combination_one += math.factorial(count_one) / (math.factorial(i) * math.factorial(count_one - i))

        ans = sum_combination_zero * sum_combination_one
        print(int(ans))