class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==0:
            l=list(n for n in range(-(n//2),(n//2)+1) if n!=0)
        else:
            l=list(n for n in range(-(n//2),(n//2)+1))
        return l
