class Solution:
    def find(self, arr, x):
        def find_first(arr, x):
            low, high = 0, len(arr) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    first = mid
                    high = mid - 1  # Keep looking left
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def find_last(arr, x):
            low, high = 0, len(arr) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    last = mid
                    low = mid + 1  # 
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [find_first(arr, x), find_last(arr, x)]