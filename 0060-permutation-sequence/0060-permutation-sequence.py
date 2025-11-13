import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans=""
        nums = [str(i) for i in range(1, n + 1)]
        k-=1
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  
            index = k // fact
            ans += nums.pop(index)
            k %= fact
        return ans
