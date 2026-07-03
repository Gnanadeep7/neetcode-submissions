class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = {}

        for i in nums:
            if i in top_k:
                top_k[i] += 1
            else:
                top_k[i] = 1
        
        result_key = sorted(top_k.keys(),key = top_k.get,reverse = True)
        
        return result_key[:k]
