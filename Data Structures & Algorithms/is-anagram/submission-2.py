class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #initialize one map for each string
        sMap = {}
        tMap = {}
        
        #edge case, can eliminate if strings are not same length
        if(len(s) != len(t)):
            return False

        #since both strs are same length, iterate thru both
        for i in range(len(s)):
            #can map items as keys and use values as counts of each item
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        for key in sMap:
            #if key in sMap is not in tMap, not anagram
            if not key in tMap.keys():
                return False
            #if counts don't align then not anagram
            if sMap[key] != tMap[key]:
                return False
        return True
