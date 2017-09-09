from collections import Counter

if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    counter_a = Counter(A)

    ans = 0
    for count in counter_a.values():
        if count % 2 != 0:
            ans += 1
    # print(counter_a.values())
    print(ans)
