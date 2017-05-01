import queue

# def exec_query(_query, _query_list):


if __name__ == '__main__':
    n = int(input())
    q = int(input())
    que = queue.Queue()
    for i in range(0, q):
        que.put(input().split())

    print(que.get())
    query_list = []
    while not que.empty():
        query = que.get()
        if query[0] == 'a':
            # ans = exec_query(query, query_list)
            query_list = []
            continue

        query_list.put(query)
