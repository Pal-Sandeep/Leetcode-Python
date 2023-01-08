class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy /= 10
        
        return x == reverse

if __name__ == "__main__":
    print Solution().isPalindrome(98789)
    print Solution().isPalindrome(36726)
    print Solution().isPalindrome(-45654)
