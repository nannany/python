O = input()
E = input()
ans = ""
if len(O) - len(E) == 0:
    for i in range(0, len(O)):
        ans += O[i]
        ans += E[i]
else:
    for i in range(0, len(E)):
        ans += O[i]
        ans += E[i]
    ans += O[-1:]

print(ans)
