from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1: Using Counter() obj
        # if len(s) != len(t):
        #     return False
        # return Counter(s) == Counter(t) # Counter retunrs a dict mapping each character to its count

        # Solution 2: Manual dict
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            counts[char] = counts.get(char, 0) - 1
        return all(count == 0 for count in counts.values())