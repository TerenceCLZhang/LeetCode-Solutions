class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        left = 0
        for _ in range(candidates):
            heapq.heappush(heap, (costs[left], left, 1))
            left += 1

        right = len(costs) - 1
        for _ in range(candidates):
            if right < left:
                break
            heapq.heappush(heap, (costs[right], right, -1))
            right -= 1

        total_cost = 0
        for _ in range(k):
            cost, _, flag = heapq.heappop(heap)
            total_cost += cost

            if left <= right:
                if flag == 1:
                    heapq.heappush(heap, (costs[left], left, 1))
                    left += 1
                else:
                    heapq.heappush(heap, (costs[right], right, -1))
                    right -= 1

        return total_cost
