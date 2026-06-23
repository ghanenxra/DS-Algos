class Solution:
    def findTwoElement(self, arr):
        repeating = -1
        missing = -1
        
        for i in range(len(arr)):
            val = abs(arr[i])
            if arr[val - 1] < 0:
                repeating = val
            else:
                arr[val - 1] = -arr[val - 1]
                
        for i in range(len(arr)):
            if arr[i] > 0:
                missing = i + 1
                break
                
        return [repeating, missing]