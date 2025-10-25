from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, target, time in times:
            adj_list[source].append((target, time))

        delay = 0
        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            delay = max(time, delay)

            for node2, time2 in adj_list[node]:
                if node2 not in visited:
                    heapq.heappush(min_heap, (time + time2, node2))

        return delay if len(visited) == n else -1
