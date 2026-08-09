class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestRes = 0

        for n in nums:
            j = 1
            if (n-1) not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1

                longestRes = max(longestRes, length )

        return longestRes
        