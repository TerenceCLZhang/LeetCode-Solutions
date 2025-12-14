class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        i = 0
        curr_gas = 0
        for j in range(len(gas)):
            curr_gas += gas[j] - cost[j]

            if curr_gas < 0:
                i = j + 1
                curr_gas = 0

        return i
