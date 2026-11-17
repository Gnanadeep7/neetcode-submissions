class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_freq , max_length = 0, 0 
        r_c = {}

        for end in range(len(s)):
            r_c[s[end]] = r_c.get(s[end],0) + 1
            max_freq = max(max_freq,r_c[s[end]])

            if k + max_freq < end - start + 1:
                r_c[s[start]] -= 1
                start += 1
            
            max_length = max(max_freq,end - start +1 )
        return max_length 
        
                                                         