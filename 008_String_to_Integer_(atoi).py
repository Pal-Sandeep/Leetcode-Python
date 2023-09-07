class Solution:
    def myAtoi(self, s: str) -> int:
        strs=s.lstrip(' _')
        result = []
        minus=False
        ch=True
        if len(strs)>=2:
            if (strs[0]=='-' or strs[0]=='+') and (strs[1]=='-' or strs[1]=='+'):
                return 0
        if len(strs)==0:
            return 0
        if strs[0]=='+':
            strs=strs[1:]
            pass 
        elif strs[0]=='-':
            minus =True
            strs=strs[1:]
        for i in range(len(strs)):
            if ord(strs[i]) in range(48,58):
                result.append(strs[i])
                ch=False
            else: break
        if ch:
            return 0
        
        r=''.join(result)
        sum= int(r) if not minus else -int(r)
        if sum > 2**31-1 or sum < -2**31:
            return 2**31-1 if not minus else -2**31
        else: return sum        
