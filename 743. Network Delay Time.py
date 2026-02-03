class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, time in times:
            adj_list[u].append((v, time))

        min_times = {}
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in min_times:
                continue

            min_times[node] = time
            for nei, nei_time in adj_list[node]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (nei_time + time, nei))

        return max(min_times.values()) if len(min_times) == n else -1
