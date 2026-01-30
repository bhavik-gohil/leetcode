class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in range(len(s)):
            if hash_map.get(s[i]) is None:
                hash_map[s[i]] = {"count": 1, "idx": i}
            else:
                hash_map[s[i]]["count"] += 1
        for k, v in hash_map.items():
            if v["count"]==1:
                return v["idx"]
        return -1


i = Solution()
call = i.firstUniqChar("aadadaad")
print("::", call)
