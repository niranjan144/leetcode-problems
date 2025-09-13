class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter=0
        for i in nums:
            if i==1:
                counter+=1
            elif i==2:
                counter+=1
            elif i%3==0:
                counter+=0
            elif i%3==1:
                counter+=1
            elif i%3==2:
                counter+=1
        return counter