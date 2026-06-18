class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {")": "(", "}": "{", "]": "["}
        myStack = []

        for i in s:
            if i in myMap.values():
                myStack.append(i)
            elif i in myMap.keys():
                if not myStack or myMap[i] != myStack.pop():
                    return False
            
        return not myStack
                

