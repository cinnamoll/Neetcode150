class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(0, len(nums), 1):
            if (target - nums[i] in index):
                return [i, index[target - nums[i]]]
            index[nums[i]] = i
        
        return []