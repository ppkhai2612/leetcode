from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The core idea relies on prefix sums.
        # A prefix sum at position j is the sum of all elements from index 0 through j.
        # If we know the prefix sum at two positions i and j (where i < j), then the subarray sum from i+1 through j is prefix[j] - prefix[i]. 
        # We want that difference to equal k.
        count = 0
        prefix_sum = 0
        seen: dict[int, int] = defaultdict(int)
        seen[0] = 1 # a prefix sum of 0 has occurred once"

        for num in nums:
            prefix_sum += num
            count += seen[prefix_sum - k]
            seen[prefix_sum] += 1

        return count