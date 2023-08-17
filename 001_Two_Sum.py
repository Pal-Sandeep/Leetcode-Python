class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_index = list(enumerate(nums))
        # nums_index.sort()
        # print(nums)
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in nums and nums.index(complement) != i:
                return [i,nums.index(complement)]
        # for i in range(len(nums)-1):
        #     j=i+1
        #     while j < len(nums):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
        #         j += 1
        #     i += 1
        # return result
