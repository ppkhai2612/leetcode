class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n)
        # Two pointers: slow and fast
        s = 1
        for f in range(1, len(nums)):
            if nums[f] != nums[f-1]:
                nums[s] = nums[f]
                s += 1

        return s