class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        len1, len2 = len(word1), len(word2)
        res = []

        while i < len1 and j < len2:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        if len1 < len2: # word1 is shorter than word2
            res.append(word2[j:])
        
        if len1 > len2: # word1 is longer than word2
            res.append(word1[i:])
        
        return "".join(res)
        
