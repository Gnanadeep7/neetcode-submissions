class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}

        for i in range(len(s)):
            s_d[s[i]] = s_d.get(s[i],0) + 1
        for j in range(len(t)):
            t_d[t[j]] = t_d.get(t[j], 0) + 1
        
        if s_d == t_d:
            return True
        else:
            return False

