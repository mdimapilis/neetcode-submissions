class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isChar(char):
            if (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9')):
                return True
            return False

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not isChar(s[i]):
                i += 1
            while j > i and not isChar(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

