# 최대유량
# 방향그래프로 생각 (물이 양방향으로 흐를 수 있음)
# 탐색을 DFS로 가장 작은 용량과 가는 길 탐색
# 작은 용량으로 채워줌
# 가는 방향은 용량으로, 반대방향은 -용량으로 (양방향 탐색을 위함)
import time

 
 

 
from collections import deque
import sys

input = sys.stdin.readline

capacity = [[0]*52 for _ in range(52)]
flow = [[0]*52 for _ in range(52)]

print("간선의 개수를 입력하세요")
N = int(input())
def int_ord(chr):
	if ord(chr) >= 97:
		return ord(chr) - 97 + 26
	return ord(chr) - 65

for _ in range(N):
	s, e, w = input().split()
	st = int_ord(s)
	ed = int_ord(e)
	weight = int(w)
	capacity[st][ed] += weight
	capacity[ed][st] += weight


def dfs(node, visit, weight):
	if node == int_ord('Z'): #Z
		que = deque()
		que.append(node)
		que.append(weight)
		return que
	for to in range(52):
		if visit[to] == False:
			w = capacity[node][to] - flow[node][to]
			if w > 0:
				w = min(w, weight)
				visit[node] = True
				res = dfs(to, visit, w)
				visit[node] = False
				if res is not None:
					res.appendleft(node)
					return res
	return None

answer = 0

while True:
    
	visit = [False]*52
	res = dfs(int_ord('A'), visit, 9999)
	if res is None:
		break
	weight = res.pop()
	st = res.popleft()
	while len(res) > 0:
		ed = res.popleft()
		flow[st][ed] += weight
		flow[ed][st] -= weight
		st = ed
	answer += weight

print("최대 유량은 " + str(answer) + " 입니다")

print("time :", time.time() - start)