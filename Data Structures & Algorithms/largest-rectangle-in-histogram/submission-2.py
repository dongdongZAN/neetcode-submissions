class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = [] # pair: (index, height)
        # maxArea = 0
        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
        #     stack.append((start, h))
        
        # for i, h in stack:
        #     maxArea = max(maxArea, h*(len(heights) - i))
        # return maxArea


        maxArea = 0
        n = len(heights)
        stack = []

        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

        

        