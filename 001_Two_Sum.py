class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in nums and nums.index(complement) != i:
                return [i,nums.index(complement)]
