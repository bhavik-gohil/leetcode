class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        arr = [""]
        last_char_space = False
        for i in s:
            if i == " ":
                last_char_space = True
            else:
                if last_char_space:
                    arr.append(i)
                else:
                    arr[-1] = arr[-1] + i
                last_char_space = False
        return len(arr[-1])
    
ins = Solution()
call = ins.lengthOfLastWord("luffy  is still    joyboy    ")
print("call: ", call)