class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)   # the ord is an inbuilt fnc from asncii 
        
        return result