import math

if __name__ == '__main__':
    N, H = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)

    max_a = max(a)
    ans = 0
    b = sorted(b, reverse=True)
    damage = 0
    for i in range(N):
        if max_a < b[i]:
            damage += b[i]
            ans += 1
        else:
            break

        if H <= damage:
            print(ans)
            exit()

    ans += math.ceil((H - damage) / max_a)

    print(ans)
