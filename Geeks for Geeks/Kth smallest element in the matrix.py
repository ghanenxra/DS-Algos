import heapq

class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, (mat[i][0], i, 0))
        
        ans = 0
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            ans = val
            if c + 1 < n:
                heapq.heappush(min_heap, (mat[r][c + 1], r, c + 1))
                
        return ans