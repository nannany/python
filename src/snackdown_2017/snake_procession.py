R = int(input())
for i in range(R):
    L = int(input())
    snake_line = list(input())
    comes_next = "H"
    ans = "Valid"
    for j in range(0, L):
        if comes_next == "H":
            if snake_line[j] == "H" and j != L - 1:
                comes_next = "T"
            elif snake_line[j] == ".":
                pass
            else:
                ans = "Invalid"
                break
        else:
            if snake_line[j] == "T":
                comes_next = "H"
            elif snake_line[j] == "H":
                ans = "Invalid"
                break
            else:
                if j == L - 1:
                    ans = "Invalid"

    print(ans)
