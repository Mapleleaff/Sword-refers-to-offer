"""
题10.2-青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

class Solution:
    def jumpFloor(self, number):
        N2=2
        N1=1
        if number<=2:
            return number
        while number>2:
            N2=N1+N2
            N1=N2-N1
            number-=1
        return N2


"""
本题扩展
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

class Solution:
    def jumpFloorII(self, number):
        return 2^(number-1)

