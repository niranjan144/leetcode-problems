class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        s=set()
        for i in nums:
            if i in s:
                a.append(i)
            else:
                s.add(i)
        return a