def pop_when_x():
    S1.pop(0)
    S2.pop(0)
    global left_state
    left_state = "X"


def pop_when_y():
    S1.pop(0)
    S1.pop(0)
    S2.pop(0)
    S2.pop(0)
    global left_state
    left_state = "Y"


if __name__ == '__main__':
    N = int(input())
    S1 = list(input())
    S2 = list(input())

    if S1[0] == S2[0]:
        cases = 3
        left_state = "X"
        pop_when_x()
    else:
        cases = 6
        left_state = "Y"
        pop_when_y()

    while len(S1) != 0:
        # print("".join(S1))
        # print("".join(S2))
        # print(cases)
        if S1[0] == S2[0]:
            state = "X"
        else:
            state = "Y"
        # print("left_state:" + left_state)
        # print("state:" + state)
        if left_state == "X" and state == "X":
            cases *= 2
            pop_when_x()
        elif left_state == "X" and state == "Y":
            cases *= 2
            pop_when_y()
        elif left_state == "Y" and state == "X":
            cases *= 1
            pop_when_x()
        elif left_state == "Y" and state == "Y":
            cases *= 3
            pop_when_y()

    print(cases % 1000000007)
