class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       set1 = set(nums1)
       set2 = set(nums2)
       newarr = set1.intersection(set2)
       newarr1 = list(newarr)
       return newarr1