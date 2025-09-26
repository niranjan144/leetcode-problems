class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ni=[]
        for i in range(len(nums)):
            ni.insert(index[i], nums[i])
        return(ni)