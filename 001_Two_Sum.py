class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            j=i+1
            while j < len(nums):
                if nums[i]+nums[j]==target:
                    return [i, j]
                j += 1
            i += 1
        return result
