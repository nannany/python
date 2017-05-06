def exchange(_A, _B, _C, _count):
    if _A % 2 == 1 or _B % 2 == 1 or _C % 2 == 1:
        return _count

    _count += 1
    tmp1 = _A / 2
    tmp2 = _B / 2
    tmp3 = _C / 2
    return exchange(tmp2 + tmp3, tmp1 + tmp3, tmp1 + tmp2, _count)


A, B, C = list(map(int, input().split()))
if A % 2 == 0 and A == B and B == C:
    print("-1")
else:
    count = 0
    ans = exchange(A, B, C, count)

    print(ans)
