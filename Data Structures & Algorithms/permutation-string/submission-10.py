class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1F, s2F = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1F[ord(s1[i]) - ord('a')] += 1 
            s2F[ord(s2[i]) - ord('a')] += 1 
        
        matches = 0
        for i in range(26):
            matches += (1 if s1F[i] == s2F[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[r]) - ord('a')
            s2F[idx] += 1
            if s1F[idx] == s2F[idx]:
                matches += 1
            elif s1F[idx] + 1 == s2F[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2F[idx] -= 1
            if s1F[idx] == s2F[idx]:
                matches += 1
            elif s1F[idx] - 1 == s2F[idx]:
                matches -= 1

            l += 1
        
        return matches == 26


        # if len(s1) > len(s2):
        #     return False

        # l, r = 0, len(s1)
        # s1F = {}
        

        # for i in range(len(s1)):
        #     s1F[s1[i]] = s1F.get(s1[i], 0) + 1
        # while r < len(s2) + 1:
        #     sub = s2[l:r]
        #     s2F = {}
        #     print(sub)
        #     for i in range(len(sub)):
        #         s2F[sub[i]] = s2F.get(sub[i], 0) + 1
        #     if s1F == s2F:
        #         return True
        #     l, r = l + 1, r + 1



        # return False