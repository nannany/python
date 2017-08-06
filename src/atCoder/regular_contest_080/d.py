if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    N = int(input())
    a = list(map(int, input().split()))

    flatten = []
    for i in range(0, N):
        flatten.append([(i + 1) for j in range(a[i])])
    flatten_2 = []
    for tmp in flatten:
        flatten_2.extend(tmp)
    # print(flatten_2)
    ans = [[] for i in range(H)]

    for i in range(0, H):
        if i % 2 == 0:
            ans[i] = list(map(str, flatten_2[i * W:(i + 1) * W]))

        else:
            ans[i] = flatten_2[i * W:(i + 1) * W]
            ans[i].reverse()
            ans[i] = list(map(str, ans[i]))

    for i in range(H):
        print(" ".join(ans[i]))
