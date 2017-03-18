inputs1 = input().split()
inputs2 = input().split()

N = int(inputs1[0])
K = int(inputs1[1])

a = []
for i in range(0, N):
    a.append(int(inputs2[i]))

a.sort(reverse=True)

i = 0
set_list = []
for i in range(0, N):
    if K < sum(a):
        target_list = [i]
        comb(a, target_list, set_list)


def comb(list, target_list, list_set):
    if K < sum(list(map(lambda x: x), list_set)):
        list_set.append(target_list)
    else:
        for i in range(target_list[len(target_list)], N):
            target_list.append(i)
            comb(list, target_list, list_set)
