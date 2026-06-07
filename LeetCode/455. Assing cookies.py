class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0   # pointer for greed array
        cookie = 0  # pointer for cookie array
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1  # child satisfied, move to next child
            cookie += 1     # always move to next cookie
        
        return child