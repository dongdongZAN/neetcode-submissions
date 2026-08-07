class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(nums[i] == nums[i+1] for i in range(0, len(nums)-1))
        