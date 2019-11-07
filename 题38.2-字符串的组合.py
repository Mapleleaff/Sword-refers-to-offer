"""
题38.2-字符串的组合
扩展习题，生成字符的所有组合
比如输入 abc，则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']，
ab 和 ba 属于不同的排列，但属于同一个组合
"""

class Solution:
    def Permutation(self, s):
        if len(s) <= 1:
            return list(s)

        s, pstr = sorted(s), []
        for i in range(len(s)):
            pstr.append(s[i])
            if i > 0 and s[i] == s[i-1]:
                continue
            for j in map(lambda x: s[i]+x, self.Permutation(s[i+1:])):
                pstr.append(j)
        return pstr

arr = 'abc'
S = Solution()
print(S.Permutation(arr))
