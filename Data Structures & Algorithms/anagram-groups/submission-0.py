class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gr_an = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in gr_an:
                gr_an[key] = []

            gr_an[key].append(i)
        return list(gr_an.values())        