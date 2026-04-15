class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        frequencies = []
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        for key in d:
            frequencies.append((key, d[key]))
        
        frequencies = sorted(frequencies, key=lambda x: x[1], reverse=True)
        answer = [key for key, v in frequencies]
        return answer[:k]