class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(sorted(nums)):
            if n not in nums_dict:
                nums_dict[n] = i
        
        res = []
        for n in nums:
            res.append(nums_dict[n])
        return res