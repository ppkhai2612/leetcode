class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # O(n)
        frequent_dict = {}
        # create a bucket with size equal to the number of inputs
        bucket = [[] for i in range(len(nums) + 1)] # O(n)

        for n in nums: # O(n)
            frequent_dict[n] = 1 + frequent_dict.get(n, 0)
        
        for n, c in frequent_dict.items(): # O(n)
            bucket[c].append(n)
        
        # run the loop backwards to get the most frequent elements
        res = []
        for i in range(len(bucket) - 1, 0, -1): # O(n)
            for ele in bucket[i]: # If the list does not have any elements, do not run the loop
                res.append(ele)
                if len(res) == k:
                    return res
            