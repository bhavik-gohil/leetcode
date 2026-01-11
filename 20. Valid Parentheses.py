map = {"(":")", "[":"]", "{":"}"}
opening = ["(", "[", "{"]
closing = [")", "]", "}"]

class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l%2 != 0:
            return False

        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if len(stack)==0 or i != map[stack[-1]]:
                    return False
                stack.pop()
        return len(stack)==0



ins = Solution()
call=ins.isValid("(){}}{")

print("call: ", call)