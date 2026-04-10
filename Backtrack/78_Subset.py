class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.n = len(nums)
        self.backtrack([], 0, nums)
        return self.res
    
    def backtrack(self, curr: List[int], first: int, nums: List[int]) -> List[List[int]]:
        self.res.append(curr[:])
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(curr, i + 1, nums)
            curr.pop()