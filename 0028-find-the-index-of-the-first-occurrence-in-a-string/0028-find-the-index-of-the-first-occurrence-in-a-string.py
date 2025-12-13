class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count=0
        for i in range(len(haystack)):
            if len(needle)==1:
                if haystack[i]==needle:
                        return(i)
                        exit()
        for i in range(len(haystack)):
            for j in range(i+1,len(haystack)):
                if haystack[i:j+1]==needle:
                    return(i)
                    count+=1
        if count==0:
            return (-1)