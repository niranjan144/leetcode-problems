class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a=[]
        s=0
        for i in range(len(nums)):
            a.append(bin(i))
        a = [x[2:] for x in a]
        indexes = [i for i, x in enumerate(a) if sum(int(bit) for bit in x) == k]
        for i in indexes:
            s+=nums[i]
        return s
        