class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ln = len(s)
        if ln != len(t):
            return False
        if s == t:
            return True

        h1 = {}
        h2 = {}
        k = ""
        i = 0
        while i < ln:
            if not h1.get(s[i]):
                if h2.get(t[i]):
                    return False
                h1[s[i]] = t[i]
                h2[t[i]] = s[i]

            k = k + h1[s[i]]
            i += 1

        print(h1)
        print(h2)
        print(k)
        return t == k


i = Solution()
call = i.isIsomorphic("egg", "add")
print(":: ", call)
