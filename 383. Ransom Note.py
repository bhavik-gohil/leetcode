class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        for char in magazine:
            mag_map[char] = mag_map[char]+1 if mag_map.get(char) else 1

        note_map = {}
        for char in ransomNote:
            note_map[char] = note_map[char]+1 if note_map.get(char) else 1
            if not mag_map.get(char) or mag_map.get(char) < note_map[char]:
                return False

        return True


i = Solution()
call = i.canConstruct("aa", "ab")
print("::", call)
