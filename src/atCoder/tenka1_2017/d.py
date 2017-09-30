if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    integers = {}
    for i in range(N):
        integer, value = list(map(int, input().split()))
        if integer in integers:
            if integers[integer] < value:
                integers[integer] = value
        else:
            integers[integer] = value

    # print(integers)

    K_bit = str(bin(K))[2:]
    # print(K_bit)
