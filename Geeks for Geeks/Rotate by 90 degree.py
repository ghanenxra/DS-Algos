class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
                
        low = 0
        high = n-1
        while low<high:
            mat[low],mat[high] = mat[high],mat[low]
            low += 1
            high -= 1
            
            
                
        