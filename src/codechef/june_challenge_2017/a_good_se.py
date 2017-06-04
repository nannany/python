if __name__ == '__main__':
    T = int(input())
    sum_set = set([3])
    ans_list = [1, 2]
    next_candidate = 3
    while len(ans_list) <= 100:
        if next_candidate in ans_list:
            next_candidate += 1
            continue

        if next_candidate not in sum_set:
            for ele in ans_list:
                sum_set.add(ele + next_candidate)
            ans_list.append(next_candidate)
            next_candidate += 1
            continue
        else:
            next_candidate += 1
            continue

    for i in range(T):
        n = int(input())

        for j in range(0, n):
            print(str(ans_list[j]), end=" ")
