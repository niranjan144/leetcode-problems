class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sum1="".join(word1)
        sum2="".join(word2)
        if sum1==sum2:
            return True
        else:
            return False
                