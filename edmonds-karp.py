from collections import defaultdict
import sys
import time

input = sys.stdin.readline

print("간선의 개수를 입력하세요")
n = int(input())
# s, t = map(str, input().split())
s, t = 'A', 'Z'
edge = defaultdict(lambda: defaultdict(int))
for _ in range(n):
    x, y, c = map(str, input().split())
    edge[x][y] += int(c)
    edge[y][x] += int(c)

start = time.time() 
def min_flow(s, t, parent):
    flow = 987654321
    while s != t:
        flow = min(flow, edge[parent[t]][t])
        t = parent[t]
    return flow


def bfs(s, t, parent):
    q = [s]
    check = defaultdict(lambda: 0)
    check[s] = 1
    while q:
        cur = q.pop(0)
        for i in edge[cur]:
            if check[i]:
                continue
            if edge[cur][i] <= 0:
                continue
            q.append(i)
            parent[i] = cur
            check[i] = 1
    if check[t]:
        return 1
    return 0


def go(s, t):
    max_flow = 0
    parent = defaultdict(lambda: -1)
    while bfs(s, t, parent):
        flow = min_flow(s, t, parent)
        max_flow += flow
        v = t
        while s != v:
            edge[parent[v]][v] -= flow
            edge[v][parent[v]] += flow
            v = parent[v]
    return max_flow


print("최대 유량은 "+str(go(s, t))+" 입니다")