class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for x in digits:
            s+=s.join(str(x))
        return [int(x) for x in str(int(s)+1)]
