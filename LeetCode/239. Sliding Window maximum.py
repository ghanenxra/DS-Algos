from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        q = deque()
        
        for i, num in enumerate(nums):
            if q and q[0] == i - k:
                q.popleft()
                
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result