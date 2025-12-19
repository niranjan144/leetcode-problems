class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        count=[]
        for i in range(len(nums)):
            if nums[i]==1:
                a+=1
            elif nums[i]==0:
                count.append(a)
                a=0
            if i==len(nums)-1:
                count.append(a)
        return max(count)