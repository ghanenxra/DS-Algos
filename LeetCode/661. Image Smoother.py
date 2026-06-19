class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                
                for i in range(max(0, r - 1), min(m, r + 2)):
                    for j in range(max(0, c - 1), min(n, c + 2)):
                        total_sum += img[i][j]
                        count += 1
                
                res[r][c] = total_sum // count
                
        return res