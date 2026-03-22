class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        num=0
        if n<=1:
            return n
        else:
            for i in range(n-1):
                num=a+b
                a=b
                b=num
            return num


