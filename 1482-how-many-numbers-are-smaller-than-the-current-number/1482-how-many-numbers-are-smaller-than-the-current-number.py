class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count1=[]
        for i in nums:
            count=0
            for j in nums:
                if i>j:
                    count+=1
                else:
                    continue
            count1.append(count)
        return count1