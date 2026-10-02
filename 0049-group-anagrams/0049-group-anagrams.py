class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # {"aet": ["eat", "tea", ...]}
        groups = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]
        
        results = []
        for val in groups.values():
            results.append(val)
        return results