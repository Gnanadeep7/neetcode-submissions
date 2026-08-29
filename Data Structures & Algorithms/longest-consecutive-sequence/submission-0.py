class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_sub  = 1
        count = 1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1
            max_sub = max(max_sub,count)
        return max_sub