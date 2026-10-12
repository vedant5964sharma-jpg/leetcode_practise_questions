
from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = [[] for _ in range(n)]

        for u, v in redEdges:
            graph[u].append((v, 0))

        for u, v in blueEdges:
            graph[u].append((v, 1))

        dist = [[-1, -1] for _ in range(n)]
        dist[0] = [0, 0]

        q = deque([(0, 0), (0, 1)])

        while q:
            u, color = q.popleft()

            for v, c in graph[u]:
                if c != color and dist[v][c] == -1:
                    dist[v][c] = dist[u][color] + 1
                    q.append((v, c))

        ans = []

        for r, b in dist:
            if r == -1:
                ans.append(b)
            elif b == -1:
                ans.append(r)
            else:
                ans.append(min(r, b))

        return ans
