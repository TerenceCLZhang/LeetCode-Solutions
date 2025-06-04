class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()

        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while (r_queue and d_queue):
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + len(senate))
            else:
                d_queue.append(d + len(senate))
        
        if (r_queue):
            return "Radiant"
        return "Dire"

# Time: O(n)
# Space: O(n)