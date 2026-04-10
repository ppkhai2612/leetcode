class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        temp_set = set() # store substring (no duplicate values)

        for r in range(len(s)): # O(n)
            # If there is a duplicate character, move left index to remove that character until the window is valid
            while s[r] in temp_set:
                temp_set.remove(s[l])
                l += 1 # move the left index
            
            w = (r - l) + 1 # calculate size of the current window
            longest = max(longest, w)
            temp_set.add(s[r]) # adding to set safety

        return longest