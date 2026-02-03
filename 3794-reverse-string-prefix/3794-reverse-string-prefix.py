class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix=""
        remain=""
        prefix=s[:k]
        remain=s[k:]       
        final=prefix[::-1]+remain
        return final