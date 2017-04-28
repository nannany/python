if __name__ == '__main__':
    n = list(input())

    back_first_ans = 0
    for i in range(0, len(n)):
        if n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '5' or n[i] == '7':
            back_first_ans += 1
        elif n[i] == '0' or n[i] == '4' or n[i] == '6' or n[i] == '9':
            back_first_ans += 3
        else:
            back_first_ans += 5
    back_first_ans += 2

    back_last_ans = 0
    for i in range(0, len(n)):
        if n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '5' or n[i] == '7':
            back_last_ans += 2
        elif n[i] == '0' or n[i] == '4' or n[i] == '6' or n[i] == '9':
            back_last_ans += 3
        else:
            back_last_ans += 4
    back_last_ans += 1

    print(min(back_first_ans, back_last_ans))
