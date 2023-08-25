class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in sorted(nums):
            if num == val:
                nums.remove(num)
                count += 1
            else:
                count += 1
        return count
