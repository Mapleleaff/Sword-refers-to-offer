"""
题44-数字序列中某一位的数字
数字以 0123456789101112131415... 的格式序列化到一个字符串中，
求任意第 n 位对应的数字。
"""

class Solution:
    def findNthDigit(self, n):
        if n < 0:
            return -1

        # digit 表示位数，个位为 1，十位为 2，百位为 3
        # base 表示每个区间的个数，如0-9为10，10-99为100，100-999为900
        digit, base = 1, 1
        while n > 9*base*digit:
            n -= 9*base*digit
            digit += 1
            base *= 10

        # 需要 n-1，因为一开始 9*base*digit只有9个，相当于少减了第0位
        curnum = str((n-1)//digit + base)
        index = (n-1) % digit

        return curnum[index]


S = Solution()
print(S.findNthDigit(11))
