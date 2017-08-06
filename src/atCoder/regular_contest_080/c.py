if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    odd_num = len([i for i in a if i % 2 == 1])
    four_divide_num = len([i for i in a if i % 4 == 0])

    if odd_num <= four_divide_num:
        print("Yes")
    else:
        if odd_num - 1 == four_divide_num and odd_num + four_divide_num == N:
            print("Yes")
        else:
            print("No")
