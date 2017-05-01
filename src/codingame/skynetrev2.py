import sys
import math
import copy

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
node = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    if n1 in node:
        node[n1].add(n2)
    else:
        tmp = {n2}
        node.update({n1: tmp})

    if n2 in node:
        node[n2].add(n1)
    else:
        tmp = {n1}
        node.update({n2: tmp})

ei = []
for i in range(e):
    ei.append(int(input()))  # the index of a gateway node

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    for gateway in ei:
        tempnode = copy.deepcopy(node)
        for target in tempnode[gateway]:
            distance_info = {}
            check_info = set()
            get_distance(tempnode,target,distance_info,check_info)

'''
node_info:ノード情報。辞書型、key:int、value:set
que:対象ノード。set
distance_info:ゲートからの距離情報。辞書型、key:int、value:int
check_info:最短距離導出済みか否か。set
'''
def get_distance(node_info,que,distance_info,check_info):
    next_que = set()
    for ele in que:
        next_que.add(ele)
        