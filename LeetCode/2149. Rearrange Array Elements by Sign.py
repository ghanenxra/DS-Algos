class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]

        ans = [0] * len(nums)

        for i in range(len(pos)):
            ans[2 * i] = pos[i]
            ans[2 * i + 1] = neg[i]

        return ans