import copy

if __name__ == '__main__':
    s = list(input())

    char_list = set(s)

    # print(char_list)


    ans = 1000
    for target_char in char_list:
        tmp_s = copy.deepcopy(s)
        tmp_ans = 0
        while True:
            if len(set(tmp_s)) == 1:
                ans = min(ans, tmp_ans)
                break

            # print(tmp_s)
            # print(target_char)
            for i in range(0, len(tmp_s) - 1):
                # print(i)
                if tmp_s[i + 1] == target_char:
                    tmp_s[i] = target_char

            tmp_s.pop(len(tmp_s) - 1)
            tmp_ans += 1


    print(ans)
