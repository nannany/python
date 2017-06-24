if __name__ == '__main__':
    N = int(input())
    a = [-1]
    for i in range(N):
        a.append(int(input()))

    count_num = 1
    next_num = a[1]
    done_num = set([1])
    while True:
        if next_num in done_num:
            print(-1)
            break
        elif next_num == 2:
            print(count_num)
            break

        count_num += 1
        done_num.add(next_num)
        next_num = a[next_num]
