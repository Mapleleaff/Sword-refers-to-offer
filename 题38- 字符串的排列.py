"""
题38- 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串 abc，则打印出由字符 a,b,c 所能排列出来的所有字符串
abc, acb, bac, bca, cab 和 cba。
"""

class Solution:
    def Permutation(self, s):
        if len(s) <= 1:
            return list(s)

        s, pstr = sorted(s), []
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            for j in map(lambda x: s[i]+x, self.Permutation(s[:i]+s[i+1:])):
                pstr.append(j)
        return pstr

arr = 'abc'
S = Solution()
print(S.Permutation(arr))
