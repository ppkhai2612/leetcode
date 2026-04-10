class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # The idea: try all centers and expand outward to get the longest palindrome

        # babad => bab
        res = ""
        res_len = 0 # length of the longest palindrome substring found so far
        s_length = len(s)

        for i in range(s_length):
            
            # odd-length palindrome
            l = r = i
            while (l >= 0 and r < s_length) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            # even-length palindrome
            l, r = i, i + 1
            while (l >= 0 and r < s_length) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res