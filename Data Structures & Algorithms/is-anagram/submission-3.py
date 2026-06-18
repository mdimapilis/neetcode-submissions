class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #base case
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for char in range(len(s)):
            sMap[s[char]] = sMap.get(s[char], 0) + 1
            tMap[t[char]] = tMap.get(t[char], 0) + 1
        
        for key in sMap:
            if not key in tMap.keys():
                return False
            if sMap[key] != tMap[key]:
                return False
        return True