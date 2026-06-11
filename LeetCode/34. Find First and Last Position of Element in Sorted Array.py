class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return bound

        start = find_bound(is_first=True)
        # If the target isn't found in the first pass, it won't exist at all
        if start == -1:
            return [-1, -1]
            
        end = find_bound(is_first=False)
        return [start, end]
