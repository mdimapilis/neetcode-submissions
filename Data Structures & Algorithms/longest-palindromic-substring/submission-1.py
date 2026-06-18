class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_copy = "#" + "#".join(s) + "#"
        lps = [0 for _ in range(len(s_copy))]
        c, r = 0, 0
        rng, ctr = 0, 0

        for i in range(len(s_copy)):
            mirror = 2*c - i
            if r > i:
                lps[i] = min(r-i, lps[mirror])
            else:
                lps[i] = 0
            try:
                while s_copy[i + 1 + lps[i]] == s_copy[i - 1 - lps[i]]:
                    lps[i] += 1
            except:
                pass
            if i + lps[i] > r:
                c = i
                r = i + lps[i]

            if lps[i] > rng:
                rng = lps[i]
                ctr = i

        start = (ctr - rng) // 2
        return s[start: start + rng]
