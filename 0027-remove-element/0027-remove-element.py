class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointers: slow and fast
        s = 0
        count = 0
        for f in range(len(nums)):
            if nums[f] != val:
                count += 1
                nums[s] = nums[f]
                s += 1
        return count