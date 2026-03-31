class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        cs=s
        for i in range(k,len(nums)):
            cs+=nums[i]-nums[i-k]
            s=max(s,cs)
        return s/k

        
