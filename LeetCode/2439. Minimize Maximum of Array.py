import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            ans = max(ans, math.ceil(prefix_sum / (i + 1)))

        return ans