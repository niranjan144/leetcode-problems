class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for j in range(2**len(nums)):
            subset = 0
            for e in range(len(nums)):
                if (j >> e) & 1 == 1:
                    subset ^= nums[e]
            result += subset
        return result
        