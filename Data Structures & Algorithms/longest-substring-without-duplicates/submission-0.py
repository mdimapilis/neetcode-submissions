class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counts = {} #<character, count>
        length = 0
        for i in range(len(s)):
            curr = 0
            for j in range(i, len(s)):
                counts[s[j]] = counts.get(s[j], 0) + 1
                print(s[j], ' ', counts[s[j]])
                if counts[s[j]] == 1:
                    curr += 1
                    length = max(length, curr)
                else:
                    counts = {}
                    break
        return length

