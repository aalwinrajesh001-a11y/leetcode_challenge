class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digsum(n):
            su=0
            while n!=0:
                su+=n%10
                n=n//10
            return su
        sum2=0
        for i in nums:
            if i>9:
                sum2+=digsum(i)
            else:
                sum2+=i
        return abs(sum(nums)-sum2)
      
