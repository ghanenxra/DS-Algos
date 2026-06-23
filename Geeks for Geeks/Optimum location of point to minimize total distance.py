import math
from typing import List

class Solution:
    def findOptimumCost(self, line: List[int], n: int, points: List[List[int]]) -> float:
        a, b, c = line[0], line[1], line[2]
        
        def compute_total_distance(x: float) -> float:
            y = -(a * x + c) / b
            
            total_dist = 0.0
            for px, py in points:
                total_dist += math.sqrt((x - px) ** 2 + (y - py) ** 2)
            return total_dist
            
        low = -1000.0
        high = 1000.0
        
        for _ in range(80):
            mid1 = low + (high - low) / 3.0
            mid2 = high - (high - low) / 3.0
            
            cost1 = compute_total_distance(mid1)
            cost2 = compute_total_distance(mid2)
            
            if cost1 < cost2:
                high = mid2
            else:
                low = mid1
                
        return round(compute_total_distance(low), 2)