class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)
        s1F = {}
        

        for i in range(len(s1)):
            s1F[s1[i]] = s1F.get(s1[i], 0) + 1
        while r < len(s2) + 1:
            sub = s2[l:r]
            s2F = {}
            print(sub)
            for i in range(len(sub)):
                s2F[sub[i]] = s2F.get(sub[i], 0) + 1
            # print(s1F)
            print(s2F)
            if s1F == s2F:
                return True
            l, r = l + 1, r + 1



        return False