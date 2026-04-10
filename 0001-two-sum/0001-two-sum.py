class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: value is value: index
        visited_nums = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in visited_nums:
                return [visited_nums[diff], i]
            visited_nums[v] = i
        
