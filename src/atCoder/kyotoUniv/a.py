if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # print(a)
    ans = 0
    tanni_sum = 0
    for ele in a:
        if tanni_sum < K:
            tanni_sum += ele
            ans += 1
        else:
            break

    if tanni_sum < K:
        print(-1)
    else:
        print(ans)
