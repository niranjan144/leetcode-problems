import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        t = n * (n + 1) // 2
        r = math.isqrt(t)
        return r if r * r == t else -1