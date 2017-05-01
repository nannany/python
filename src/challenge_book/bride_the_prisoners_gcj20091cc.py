import queue

if __name__ == '__main__':
    T = int(input())
    P, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    que = queue.PriorityQueue()
