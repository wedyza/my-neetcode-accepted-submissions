class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        frequencies = []
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        for key in d:
            frequencies.append((d[key], key))
        
        frequencies = sorted(frequencies)
        answer = [key for v, key in frequencies[::-1]]
        return answer[:k]