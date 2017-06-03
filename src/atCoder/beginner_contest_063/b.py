S = list(input())
no_dup = set(S)
# print(S)
# print(no_dup)
# print(len(no_dup))

if len(S) == len(no_dup):
    print("yes")
else:
    print("no")
