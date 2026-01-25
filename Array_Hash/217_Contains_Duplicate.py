#convert sang set roi so sanh
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if (len(nums_set) != len(nums)):
            return True
        return False
    
#sort roi so sanh cac phan tu canh nhau
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        for i in range(0, length - 1, 1):
            if (nums[i] == nums[i + 1]):
                return True
        
        return False