N = int(input())

tree = [[] for i in range(N)]
for i in range(N - 1):
    tmp1, tmp2 = list(map(int, input().split()))
    tree[tmp1 - 1].append(tmp2 - 1)
    tree[tmp2 - 1].append(tmp1 - 1)

one_tree = list(filter(lambda x: len(x) == 1, tree))
two_tree = list(filter(lambda x: len(x) == 2, tree))

new_tree = []
for ele in one_tree:
    new_tree.append(ele[0])

no_dup_tree = list(set(new_tree))

if len(no_dup_tree) != len(new_tree):
    print("First")
else:
    print("Second")
