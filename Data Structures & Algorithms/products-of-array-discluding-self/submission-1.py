class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        total = 1
        for n in nums:
            total *= n
        for i in range(len(nums)):
            if total != 0:
                res[i] = int(total / nums[i])
            elif nums[i] != 0:
                res[i] = 0
            else:
                for j in range(len(nums)):
                    if j != i:
                        res[i] *= nums[j]
            
        return res
                
        