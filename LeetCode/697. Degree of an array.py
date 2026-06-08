class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}   # frequency
        first = {}   # first occurrence index
        last = {}    # last occurrence index
        
        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1
            if n not in first:
                first[n] = i
            last[n] = i
        
        degree = max(count.values())
        
        res = float('inf')
        for n, freq in count.items():
            if freq == degree:
                res = min(res, last[n] - first[n] + 1)
        
        return res