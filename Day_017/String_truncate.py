class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=list()
        l=s.split(" ")
        st=""
        for i in range (0,k):
            st=st+l[i]+" "
        return st[:-1]
