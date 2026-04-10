class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {} # store the traversed elements in the list
        for i, char in enumerate(nums):
            if char in hashmap:
                if i - hashmap[char] <= k:
                    return True
            hashmap[char] = i
        
        return False