class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def sliding_window(l1: int, l2: int) -> int:

            max_left = curr_left = sum(nums[:l1]) # left window: [0, l1-1]
            curr_right = sum(nums[l1:l1 + l2]) # right window: [l1, l1+l2-1]
            res = max_left + curr_right
            
            # Slide windows: left ends at i, right starts at i+1
            for i in range(l1, len(nums) - l2):
                # Slide left window to end at i
                curr_left += nums[i] - nums[i - l1]
                max_left = max(max_left, curr_left)
                
                # Slide right window to start at i+1
                curr_right += nums[i + l2] - nums[i]
                
                # Combine best left (ending ≤ i) with current right (starting at i+1)
                res = max(res, max_left + curr_right)
            
            return res

        # since either window length could come first, we run this function twice to take the maximum
        return max(
            sliding_window(firstLen, secondLen),
            sliding_window(secondLen, firstLen)
        )