class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts=[0]*26
        s2_counts=[0]*26

        for c in s1:
            s1_counts[ord(c)-97]+=1
        print(s1_counts)

        ln=len(s1)
        x=0

        for i, c in enumerate(s2):
            s2_counts[ord(c)-97]+=1
            if s1_counts==s2_counts:
                return True

            if i-ln>=0:
                print("-",c, i, i-ln,  s2_counts)
                s2_counts[ord(s2[i-ln])-97]-=1
                if s1_counts==s2_counts:
                    return True
                
            
        print(s2_counts)

        return False


i = Solution()
call = i.checkInclusion("ab", "eidaoo")
print(":: ", call)
