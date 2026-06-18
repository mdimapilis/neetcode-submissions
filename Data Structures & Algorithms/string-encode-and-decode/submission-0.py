class Solution:
#also a design question
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #adds len of each string and delimiter 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #iterates through idx i and j (not inclusive)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        return res
