class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        a=nums[0:n]
        b=nums[n:]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c