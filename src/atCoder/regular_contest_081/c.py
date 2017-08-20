if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    tmp_max_square = 0
    tmp_max_dup_1 = 0
    tmp_max_dup_2 = 0
    while len(A) != 0:
        tmp = A[0]
        tmp_count = A.count(tmp)
        # print(tmp_count)
        if tmp_count >= 4:
            if tmp_max_square < tmp:
                tmp_max_square = tmp

            if tmp_max_dup_2 < tmp < tmp_max_dup_1:
                tmp_max_dup_2 = tmp
            elif tmp_max_dup_1 <= tmp:
                tmp_max_dup_2 = tmp_max_dup_1
                tmp_max_dup_1 = tmp
        elif tmp_count >= 2:
            if tmp_max_dup_2 < tmp < tmp_max_dup_1:
                tmp_max_dup_2 = tmp
            elif tmp_max_dup_1 <= tmp:
                tmp_max_dup_2 = tmp_max_dup_1
                tmp_max_dup_1 = tmp

        for i in range(tmp_count):
            A.remove(tmp)

    square_ans = tmp_max_square * tmp_max_square
    rectan_ans = tmp_max_dup_1 * tmp_max_dup_2
    if square_ans < rectan_ans:
        print(rectan_ans)
    else:
        print(square_ans)
