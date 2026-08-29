class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def ways(n):
            if n <= 2:
                return n

            if n in dp:
                return dp[n]
            
            dp[n] = ways(n-1) + ways(n-2)

            return dp[n]
        return ways(n)