class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)
        # total = 1
        # for n in nums:
        #     total *= n
        # for i in range(len(nums)):
        #     if total != 0:
        #         res[i] = total // nums[i]
        #     elif nums[i] != 0:
        #         res[i] = 0
        #     else:
        #         for j in range(len(nums)):
        #             if j != i:
        #                 res[i] *= nums[j]
        # return res

        # res = [1]*len(nums)

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        
        # postfix = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        
        # return res

        length = len(nums)
        res = [0] * length
        pref = [0] * length
        suff = [0] * length

        pref[0] = suff[length-1] = 1

        for i in range(1, length):
            pref[i] = nums[i-1]*pref[i-1]
        for i in range(length-2, -1, -1):
            suff[i] = nums[i+1]*suff[i+1]
        for i in range(length):
            res[i] = pref[i] * suff[i]
        
        return res



                
        