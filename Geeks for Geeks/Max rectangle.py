class Solution:
    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0
            
        n = len(mat)
        m = len(mat[0])
        
        def max_histogram_area(heights):
            stack = []
            max_area = 0
            index = 0
            while index < len(heights):
                if not stack or heights[index] >= heights[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    top_of_stack = stack.pop()
                    area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                    max_area = max(max_area, area)
            
            while stack:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
                
            return max_area

        current_row = [0] * m
        max_rectangle_area = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    current_row[j] += 1
                else:
                    current_row[j] = 0
            
            max_rectangle_area = max(max_rectangle_area, max_histogram_area(current_row))
            
        return max_rectangle_area