class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write = 0 # tracks where the next non-zero goes.
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        while write < n: # fills positions write through n-1 with zeros.
            nums[write] = 0
            write += 1