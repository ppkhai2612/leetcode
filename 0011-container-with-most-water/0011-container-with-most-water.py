class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) time
        # set two pointer (left and right)
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r: # when leff >= right, loop ends

            # calculate the area
            w = r - l
            h = min(height[l], height[r])
            current_area = w * h

            # update max area
            max_area = max(max_area, current_area)

            # update left and right pointers
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
