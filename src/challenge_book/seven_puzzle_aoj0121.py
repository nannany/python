from collections import deque
import copy

swap = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5], [1, 4, 6], [2, 5, 7], [3, 6]]


def bfs():
    ia = list(range(8))
    count = {str(ia): 0}
    que = deque()
    que.append((ia, 0))
    while len(que) != 0:
        state, cnt = que.popleft()
        # pos:0の位置
        pos = state.index(0)
        swap_target = swap[pos]
        for i in swap_target:
            tmp_state = copy.copy(state)
            tmp_state[i], tmp_state[pos] = tmp_state[pos], tmp_state[i]
            if str(tmp_state) not in count:
                count[str(tmp_state)] = cnt + 1
                que.append((tmp_state, cnt + 1))
    return count


if __name__ == '__main__':
    count = bfs()
    while True:
        try:
            prob = list(map(int, input().split()))
            print(count[str(prob)])
        except:
            break
