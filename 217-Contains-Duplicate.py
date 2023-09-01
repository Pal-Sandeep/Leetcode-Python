class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        nums[:]=sorted(nums)        
        return any(nums[i]==nums[i+1] for i in range(length-1))
