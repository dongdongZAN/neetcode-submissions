class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res

        # while left < right:
        #     res = max(res, min(heights[left], heights[right]) * (right - left))
        #     if heights[left] <= heights[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return res

        