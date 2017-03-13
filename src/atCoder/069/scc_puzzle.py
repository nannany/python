two_input = input().split()

s = int(two_input[0])
c = int(two_input[1])

while (s + 1) * 2 <= c - 2:
    s += 1
    c -= 2

print(s)
