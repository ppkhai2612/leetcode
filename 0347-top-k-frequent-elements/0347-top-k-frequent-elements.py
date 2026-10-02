from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        # the length of bucket is n + 1
        # index i will hold all elements that appeared exactly i times.
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)

        # Walk the buckets array from the end (highest frequency) to the start,
        # collecting elements until we have k.
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result