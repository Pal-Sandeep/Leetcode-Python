# Leetcode-Python
Leetcode Solutions
import re
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        s=s.replace('IV', 'IIII').replace('IX','IIIIIIIII')
        s=s.replace('XL', 'XXXX').replace('XC','XXXXXXXXX')
        s=s.replace('CD', 'CCCC').replace('CM','CCCCCCCCC')
        m = s.split('M')
        d = s.split('D')
        c = s.split('C')
        l = s.split('L')
        x = s.split('X')
        v = s.split('V')
        i = s.split('I')
        # print(m, d, c,l,x,v,i)
        print(s)
        L = []
        temp = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                temp += s[i]
            else:
                L.append(temp)
                temp = s[i]
            if i == len(s)-1:
                L.append(temp)
        sum = 0
        for i in L:
            print(i)
            if i[0] == 'M':
                sum += roman['M'] * len(i)
            elif i[0] =='C':
                sum += roman['C'] * len(i)
            elif i[0] =='D':
                sum += roman['D'] * len(i)
            elif i[0] =='L':
                sum += roman['L'] * len(i)
            elif i[0] =='X':
                sum += roman['X'] * len(i)
            elif i[0] =='V':
                sum += roman['V'] * len(i)
            elif i[0] =='I':
                sum += roman['I'] * len(i)
        return sum