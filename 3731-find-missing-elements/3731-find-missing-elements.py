class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        miss=[]
        nums.sort()
        for i in range(nums[0],nums[-1]):
            if i in nums:
                continue
            else:
                miss.append(i)
        return(miss)