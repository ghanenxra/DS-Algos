class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}  # frequency map of nums2
        for n in nums2:
            self.freq[n] = self.freq.get(n, 0) + 1

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        # remove old value from freq map
        self.freq[old] -= 1
        if self.freq[old] == 0:
            del self.freq[old]
        # add new value
        self.nums2[index] += val
        new = self.nums2[index]
        self.freq[new] = self.freq.get(new, 0) + 1

    def count(self, tot: int) -> int:
        result = 0
        for n in self.nums1:
            complement = tot - n
            result += self.freq.get(complement, 0)
        return result