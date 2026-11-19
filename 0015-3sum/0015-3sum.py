class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = [] 
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicate
                continue
            if nums[i] > 0: # Since the array is sorted, if the current element > 0, then its sum with any subsequent elements cannot possibly equal 0.
                break

            left, right = i + 1, n - 1
            target = -nums[i]
            while left < right:
                current = nums[left] + nums[right]
                if current == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]: # skip duplicate
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: # skip duplicate
                        right -= 1

                    left += 1
                    right -= 1

                elif current < target:
                    left += 1
                else:
                    right -= 1

        return result