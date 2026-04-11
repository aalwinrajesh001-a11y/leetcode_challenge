class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=set(nums)
        for i in l:
            if nums.count(i)==1:
                return i
              
