# def max_path(_s):
#     d[_s] = 0
#     while True:
#         update = False
#         for i in range(1, M):
#             edge = abc[i]
#             if


N, M = list(map(int, input().split()))
abc = [[] for i in range(N)]
for i in range(M):
    a, b, c = list(map(int, input().split()))
    abc[a].append([b, c])

print(abc)

d = [-float("inf") for i in range(N + 1)]
