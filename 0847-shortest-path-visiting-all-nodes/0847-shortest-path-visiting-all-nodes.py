from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)

        if n == 1:
            return 0

        target = (1 << n) - 1

        queue = deque()
        visited = set()

        # Start BFS from every node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, distance = queue.popleft()

            # All nodes have been visited
            if mask == target:
                return distance

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)

                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    queue.append((neighbor, new_mask, distance + 1))

        return -1
        