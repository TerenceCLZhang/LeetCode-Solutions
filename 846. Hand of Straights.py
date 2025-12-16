class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        counter = Counter(hand)
        heap = [v for v in counter.keys()]
        heapq.heapify(heap)

        while heap:
            num = heap[0]

            for curr_num in range(num, num + groupSize):
                if curr_num not in counter:
                    return False

                counter[curr_num] -= 1

                if counter[curr_num] == 0:
                    del counter[curr_num]
                    heapq.heappop(heap)

        return True
