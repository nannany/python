from collections import deque
import sys

if __name__ == '__main__':
    s = list(input())
    que = deque(s)

    ans = 0
    while len(que) != 0:
        if que[0] == que[-1]:
            if len(que) == 1:
                que.pop()
            else:
                que.popleft()
                que.pop()
        elif que[0] != "x" and que[-1] != "x":
            print(-1)
            sys.exit()
        else:
            if que[0] == "x":
                que.append("x")
                ans += 1
            elif que[-1] == "x":
                que.appendleft("x")
                ans += 1

    print(ans)
