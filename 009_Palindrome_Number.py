class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        return True if str(temp) == str(x)[::-1] else False
