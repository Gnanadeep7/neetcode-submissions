class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            # If the current element is already in the window, we found a match
            if nums[i] in seen:
                return True
            
            # Add the current element to the window
            seen.add(nums[i])
            
            # Keep the window size at most k by removing the oldest element
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False