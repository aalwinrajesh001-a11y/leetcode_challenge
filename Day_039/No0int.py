class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        l=[i for i in range(1,n) if '0' not in str(i)]
        
        for i in l:
            
            if n-i in l:
                
                return [i,n-i]
        
