class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num ** 0.5)
        return root * root == num