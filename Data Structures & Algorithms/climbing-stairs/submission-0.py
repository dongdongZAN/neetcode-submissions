class Solution:
    def climbStairs(self, n: int) -> int:
        """
        2. Dynamic Programming (Top-Down)
        """
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)

        