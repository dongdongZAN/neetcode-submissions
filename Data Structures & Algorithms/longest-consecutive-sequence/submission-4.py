class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestRes = 0

        for num in nums:
            j = 1
            if (num - 1) not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1

                longestRes = max(longestRes, length )

        return longestRes


        
        