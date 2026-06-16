class Solution:
    def commonElements(self,a ,b ,c):
        n1, n2, n3 = len(a), len(b), len(c)
        i = j = k = 0
        result = []
        
        while i < n1 and j < n2 and k < n3:
            if a[i] == b[j] == c[k]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                    
                i += 1
                j += 1
                k += 1
                
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1
            
        return result
                