class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Instead of calculating the sum of each subarray, 
        # we only calculate the sum of the first window, then update the sum when sliding window
        curr_window = res = sum(nums[:k]) # sum of the first window

        for i in range(k, len(nums)):
            curr_window += nums[i] - nums[i-k]
            res = max(res, curr_window)

        return res / k