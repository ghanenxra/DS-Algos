class Solution:
    def sortedMatrix(self, mat):
        n = len(mat)
        flat_list = []
        for row in mat:
            flat_list.extend(row)
        
        flat_list.sort()
        
        idx = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = flat_list[idx]
                idx += 1
                
        return mat