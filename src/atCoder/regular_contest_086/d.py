if __name__ == '__main__':
    N = int(input())
    tmp = list(map(int, input().split()))
    a = [0]
    a = a + tmp
    target_idx = 1
    ans_list = []
    m = 0
    while target_idx != N:
        if a[target_idx] > a[target_idx + 1]:
            m += 1
            if a[target_idx] > 0:
                a[target_idx + 1] += a[target_idx]
                ans_list.append((target_idx, target_idx + 1))
            else:
                a[target_idx] += a[target_idx + 1]
                ans_list.append((target_idx + 1, target_idx))
        else:
            target_idx += 1

    print(m)
    for x,y in ans_list:
        print(str(x) + " " + str(y))