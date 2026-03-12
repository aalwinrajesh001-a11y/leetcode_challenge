class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        su=0
        n=x
        while n!=0:
            su+=n%10
            n=n//10
        if x%su==0:
            return su
        else:
            return -1
