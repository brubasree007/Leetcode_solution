from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]  # (cost, node, consecutive_count)

        dist = {(0, 1): 0}

        while pq:
            cost, u, cnt = heappop(pq)

            if u == n - 1:
                return cost

            if cost > dist.get((u, cnt), float('inf')):
                continue

            for v, w in graph[u]:

                if labels[v] == labels[u]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + w

                state = (v, new_cnt)

                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost
                    heappush(pq, (new_cost, v, new_cnt))

        return -1
