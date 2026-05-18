class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            seen[i] = 1 + seen.get(i,0)
        
        arr = []
        for i, j in seen.items():
            arr.append([j,i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res