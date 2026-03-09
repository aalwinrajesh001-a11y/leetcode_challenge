class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def pdct(n):
            pdct=1
            while n!=0:
                num=n%10
                pdct=pdct*num
                n=n//10
            return pdct
        def su(n):
            su_=0
            while n!=0:
                num=n%10
                su_+=num
                n=n//10
            return su_
        return pdct(n)-su(n)



