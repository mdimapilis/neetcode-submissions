class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
            
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#           
#         if not strs:
#             return ""
#         sizes, res = [], ""
#         for s in strs:
#             sizes.append(len(s))
#         for sz in sizes:
#             res += str(sz)
#             res += ','
#         res += '#'
            # res = "X,X,X,X,X,#" X = length of each word
#         for s in strs:
#             res += s
            # res = "X,X,X,X,X,#word1word2word3"
#         return res

#     def decode(self, s: str) -> List[str]:
            #  s = res = "X,X,X,X,X,#word1word2word3"
#         if not s:
#             return []
#           sizes and res are arrays while i is ptr at pos 0
#         sizes, res, i = [], [], 0
            # look at numbers until delimiter '#'
            # cur collects len(words)
#         while s[i] != '#':
#             cur = ""
#             while s[i] != ',':
#                 cur += s[i]
#                 i += 1 --> moves pointer 1 pos right, maybe len(word) > 9
#             sizes.append(int(cur)) --> once size is attained, append size to sizes
#             i += 1 --> move to next len once we reach ','
#         i += 1 --> move pointer to actual words now
            # iterate thru sizes array and append word to res array
#         for sz in sizes:
            # use array slicing, starting at i which should be first pos after '#' then cut at sizing 
#             res.append(s[i:i + sz])
#             i += sz
#         return res
