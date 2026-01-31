from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        hash_map = {0: 1}

        for n in nums:
            prefix_sum += n

            if hash_map.get(prefix_sum-k) is not None:
                cnt += hash_map[prefix_sum-k]

            hash_map[prefix_sum] = hash_map[prefix_sum] + \
                1 if hash_map.get(prefix_sum) else 1

        return cnt


i = Solution()
# call = i.subarraySum([1, 2, 3], 3)
# call = i.subarraySum([1, 1, 1], 2)
# call = i.subarraySum([1], 1)
call = i.subarraySum([1, 2, 1, 2, 1], 3)
# call = i.subarraySum([-1, -1, 1], 0)
# call = i.subarraySum([1, -1, 0], 0)  # 3
print("::", call)


1
