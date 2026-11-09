class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dic = {}
        t_dic = {}

        for i in s:
            s_dic[i] = s_dic.get(i,0) + 1
        for j in t:
            t_dic[j] = t_dic.get(j,0) + 1
        
        return s_dic == t_dic
                

