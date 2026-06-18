class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if lengths are different, return False if so
        if (len(s) != len(t)):
            return False
        sFreq = {}
        tFreq = {}

        # same length
        #keys = 
        for char in range(len(s)):
            sFreq[s[char]] = sFreq.get(s[char], 0) + 1
            tFreq[t[char]] = tFreq.get(t[char], 0) + 1

        #keys/chars are the same, so just need to check freqs
        if(sFreq.keys() == tFreq.keys()):
            for key in sFreq:
                if sFreq[key] != tFreq[key]:
                    return False
            return True
        return False