class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        for n in nums:
            total *= n
        for i in range(len(nums)):
            if total != 0:
                res.append(int(total / nums[i]))
            elif nums[i] != 0:
                res.append(0)
            else:
                t = 1
                for j in range(len(nums)):
                    if j != i:
                        t *= nums[j]
                res.append(t)
            
        
        return res
                
        