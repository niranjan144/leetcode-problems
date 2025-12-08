class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                d = a*a + b*b
                c = int(d**0.5)   
                if c <= n and c*c == d:
                    count += 1
        return count