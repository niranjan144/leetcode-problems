import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = [1] * n
        left = 1
        for i in range(n):
            c[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            c[i] *= right
            right *= nums[i]
        return(c)