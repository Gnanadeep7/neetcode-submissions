class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        start = 0
        max_length = 0 

        for end in range(len(s)):
            while s[end] in unique_char:
                unique_char.remove(s[start])
                start += 1

            unique_char.add(s[end])
            length = end - start + 1
            max_length = max(max_length,length)

        return max_length
