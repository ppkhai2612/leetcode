class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3: # if there are only 2 bars, it cannot hold water.
            return 0
        left, right = 0, len(height) - 1
        # left_max: stores the maximum height encountered by the left pointer
        # right_max: stores the maximum height encountered by the right pointer
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            # logic: process the side that has the lower maximum value
            if left_max <= right_max: 
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water