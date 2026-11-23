class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        write = n - 1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq >= right_sq:
                result[write] = left_sq
                left += 1
            else:
                result[write] = right_sq
                right -= 1
            write -= 1
        return result