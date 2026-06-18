class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counts = {} #<character, count>
        length = 0

        l, r = 0, 0
        curr = 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
            r += 1
        return length


        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1

            # If duplicate, shrink from the left
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1

            # Update max length
            length = max(length, r - l + 1)
            r += 1

        return length

        # for i in range(len(s)):
        #     curr = 0
        #     for j in range(i, len(s)):
        #         counts[s[j]] = counts.get(s[j], 0) + 1
        #         if counts[s[j]] == 1:
        #             curr += 1
        #             length = max(length, curr)
        #         else:
        #             counts = {}
        #             break
        # return length

