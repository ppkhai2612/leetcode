class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution #1: O(n)
        # i: index, v: value
        visited_nums = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in visited_nums:
                return [visited_nums[diff], i]
            visited_nums[v] = i

        # Solution #2: O(n^2)
        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        #     for i in range(len(nums)):
        #         for j in range(i+1, len(nums)):
        #             if (nums[i] + nums[j]) == target:
        #                 return [i, j]