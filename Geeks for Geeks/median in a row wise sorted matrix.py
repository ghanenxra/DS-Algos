from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = min(mat[i][0] for i in range(n))
        high = max(mat[i][-1] for i in range(n))
        
        desired_count = (n * m + 1) // 2
        
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for i in range(n):
                count += bisect_right(mat[i], mid)
                
            if count < desired_count:
                low = mid + 1
            else:
                high = mid - 1
                
        return low