from collections import Counter

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)
    ans = 0
    for ele, count in counter.items():
        if ele < count:
            ans += count - ele
        elif count < ele:
            ans += count

    print(ans)
