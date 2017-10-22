import sys


def is_kaibun(mojiretu):
    for i in range(0, len(mojiretu) // 2):
        if mojiretu[i] != mojiretu[len(mojiretu) - (i + 1)]:
            return False

    return True


if __name__ == '__main__':
    s = input()
    if not is_kaibun(s.replace("x", "")):
        print(-1)
        sys.exit()

    s_rev = s[::-1]

    target = 0
    ans = 0
    s_list = list(s)
    s_rev_list = list(s_rev)
    while True:
        if len(s) // 2 < target:
            break

        if s_list[target] == s_rev_list[target]:
            target += 1
            continue
        elif s_list[target] == "x":
            s_rev_list.insert(target, "x")
            s_list.insert(len(s_list) - target, "x")
            ans += 1
            target += 1
        elif s_rev_list[target] == "x":
            s_list.insert(target, "x")
            s_rev_list.insert(len(s_rev_list) - target, "x")
            ans += 1
            target += 1

    print(ans)
