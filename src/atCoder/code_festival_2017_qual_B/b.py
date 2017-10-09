from collections import Counter

if __name__ == '__main__':
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    counter_d = Counter(D)
    counter_t = Counter(T)

    ans = "YES"
    for point, num in counter_t.items():
        if counter_d.get(point) is None or counter_d.get(point) < num:
            ans = "NO"
            break

    print(ans)
