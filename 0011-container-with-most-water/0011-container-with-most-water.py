class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) time
        # set two pointers (left and right)
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r: # when leff >= right, area = 0

            l_height = height[l]
            r_height = height[r]

            # calculate the current area
            w = r - l
            h = min(l_height, r_height)
            current_area = w * h

            # update max area
            max_area = max(max_area, current_area)

            # update left and right pointers
            if l_height < r_height:
                l += 1
            else:
                r -= 1

        return max_area