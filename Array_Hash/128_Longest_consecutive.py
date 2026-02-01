class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in num_set:
                y = i + 1
                while y in num_set:
                    y+=1
                res = max(res, y - i)

        return res