from  collections import Counter

if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    a = []
    for i in range(H):
        a.extend(input())

    counter = Counter(a)

    value_divide_by_4 = []
    for i in counter.values():
        value_divide_by_4.append(i % 4)
    # print(value_divide_by_4)

    ans = "Yes"
    cnt_odd = 0
    cnt_even = 0
    if H % 2 == 0 and W % 2 == 0:
        for i in value_divide_by_4:
            if i != 0:
                ans = "No"
                break
    elif H % 2 != 0 and W % 2 != 0:
        # cnt_odd = 0
        # cnt_even = 0
        accept = (H - 1) // 2 + (W - 1) // 2
        for i in value_divide_by_4:
            if i == 1:
                cnt_odd += 1
            elif i == 3:
                cnt_odd += 1
                cnt_even += 1
            elif i == 2:
                cnt_even += 1

            if cnt_odd >= 2:
                ans = "No"
                break
            elif cnt_even > accept:
                ans = "No"
                break
    else:
        if H % 2 == 0:
            accept = H // 2
        else:
            accept = W // 2

        for i in value_divide_by_4:
            if i == 1:
                cnt_odd += 1
            elif i == 3:
                cnt_odd += 1
                cnt_even += 1
            elif i == 2:
                cnt_even += 1

            if cnt_odd >= 2:
                ans = "No"
                break
            elif cnt_even > accept:
                ans = "No"
                break

    print(ans)
