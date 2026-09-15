class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first,second = 0,0

        for i in cost:
            current_cost = i + min(first,second)
            first , second = second , current_cost
        
        return min(first,second)