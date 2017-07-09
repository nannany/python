if __name__ == '__main__':
    N, A, B, C, D = list(map(int, input().split()))
    if C + D == 0:
        if A == B:
            print("YES")
        else:
            print("NO")
    else:
        average_c_d = (C + D) / 2

        range_c_d = (D - C) / 2

        ul = A - average_c_d * (N - 1)

        target_index = round((B - ul) / (C + D))

        if target_index < 0:
            target_index = 0
        elif N - 1 < target_index:
            target_index = N - 1

        under = ul + (C + D) * target_index - range_c_d * (N - 1)
        upper = ul + (C + D) * target_index + range_c_d * (N - 1)

        if under <= B <= upper:
            print("YES")
        else:
            print("NO")
