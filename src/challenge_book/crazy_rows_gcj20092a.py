def judge_last_one_location(_last_one_location):
    for k in range(len(_last_one_location)):
        if k < _last_one_location[k]:
            return True
    else:
        return False


def swap(_last_one_location, _j, _l):
    tmp = _last_one_location[l]
    for k in range(0, _l - _j):
        _last_one_location[_l - k] = _last_one_location[_l - k - 1]

    _last_one_location[_j] = tmp

    return _last_one_location


if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        matrix = [list(input()) for j in range(N)]
        last_one_location = []
        for zero_one_list in matrix:
            for j in range(0, N):
                if zero_one_list[N - 1 - j] == '1' or N - 1 - j == 0:
                    last_one_location.append(N - 1 - j)
                    break

        count = 0
        while judge_last_one_location(last_one_location):
            for j in range(0, N):
                if j < last_one_location[j]:
                    for l in range(j + 1, N):
                        if last_one_location[l] <= j:
                            count += l - j
                            last_one_location = swap(last_one_location, j, l)
                            break

        print("Case #" + str(i) + ": " + str(count))
