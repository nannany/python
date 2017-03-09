import re

first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

n_list = []
for i in range(n):
    n_list.append(input())
m_list = []
for i in range(m):
    m_list.append(input())

if m == n:
    if n_list == m_list:
        print("Yes")
    else:
        print("No")
else:
    match_flg = False
    for i in range(0, n - m):
        matchOb = re.match(m_list[0], n_list[i])
        if matchOb:
            start_pos = matchOb.start()
            end_pos = matchOb.end()
            for j in range(0, m):
                if n_list[i + j][start_pos:end_pos] == m_list[j] and j == m - 1:
                    match_flg = True
                elif n_list[i + j][start_pos:end_pos] != m_list[j]:
                    break

if match_flg:
    print("Yes")
else:
    print("No")
