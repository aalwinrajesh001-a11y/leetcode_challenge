class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=int("".join(map(str,digits)))+1
        digits.clear()
        digits.extend(int(d) for d in str(number))
        return digits
        
