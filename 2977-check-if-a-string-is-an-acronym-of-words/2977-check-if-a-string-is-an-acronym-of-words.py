class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        f=[]
        if len(words)==len(s):
            for i in words:
                f.append(i[0])
        fs="".join(f)
        return(fs==s)