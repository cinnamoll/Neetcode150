class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for i, c in count.items():
            freq[c].append(i)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if (k == 0):
                    break
                res.append(j)
                k-=1

        return res