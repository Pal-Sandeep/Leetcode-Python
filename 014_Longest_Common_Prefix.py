class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=''
        strs[:]=sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]: return common
            else: common+=first[i]
        return common
