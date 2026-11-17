class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_count = 0
        start = 0

        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end],0) + 1
            while seen[s[end]] > 1:
                seen[s[start]] -=1
                start += 1
            
            max_count = max(max_count,end - start + 1 )
        return max_count