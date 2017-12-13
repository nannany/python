import collections

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ele_count = len(set(A))
    # print(ele_count)

    counter = collections.Counter(A)
    ans = 0
    for ele in counter.most_common()[:-(ele_count - K + 1):-1]:
        ans += ele[1]

    print(ans)
