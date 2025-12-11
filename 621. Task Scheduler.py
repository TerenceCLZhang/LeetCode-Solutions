class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        heap = [-v for v in counter.values()]
        heapq.heapify(heap)

        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                t = heapq.heappop(heap) + 1
                if t < 0:
                    queue.append((t, time + n))

            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(heap, count)

        return time
