from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)
        while i > m:
            nums1.pop(i-1)
            i = i - 1
        if m == 0:
            nums1.extend(nums2)
            nums2 = []

        print("nums1, nums2", nums1, nums2)

        if len(nums2) > 0:
            i = m-1
            j = n-1
            while j >= 0 and i >= 0:
                print("i, j", i, j)
                print("nums1[i], nums2[j]", nums1[i], nums2[j])
                print("nums1, nums2", nums1, nums2)
                if nums1[i] <= nums2[j]:
                    nums1.insert(i+1, nums2[j])
                    nums2.pop(j)
                    j = j-1
                else:
                    if i == 0 and nums1[i] >= nums2[j]:
                        nums1.insert(i, nums2[j])
                        nums2.pop(j)
                        j = j-1
                    else:
                        i = i-1

        print("--nums1", nums1)


ins = Solution()
call = ins.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
print("call: ", call)
