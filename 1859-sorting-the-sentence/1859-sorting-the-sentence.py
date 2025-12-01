class Solution:
    def sortSentence(self, s: str) -> str:
        a=dict()
        final=""
        b=s.split()
        last=[i[-1] for i in b]
        rest=[i[:-1] for i in b]
        a=dict(zip(last,rest))
        for i in range(1,len(rest)+1):
            final+=a[str(i)]+" "
        return(final[:-1])