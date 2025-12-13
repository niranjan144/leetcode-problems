class Solution:
    def reverseWords(self, s: str) -> str:
        r=""
        final=""
        r=s.split()
        rr=r[::-1]
        for i in rr:
            final+=i+" "
        return final[:-1]