class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros , ones , twos = [], [], []

        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num == 1:
                ones.append(num)
            else:
                twos.append(num)
        nums[:] = zeros + ones + twos
        return nums