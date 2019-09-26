"""
题16-数值的整数次方
给定一个 double 类型的浮点数 base 和 int 类型的整数 exponent。
求 base 的 exponent 次方。
"""

class WithExponent:
    def Power(self, base, exponent):

        if abs(base - 0) < 0.0001:
            return None

        if exponent == 0:
            return 0

        if exponent == 1:
            return base

        if exponent == -1:
            return 1/base

        result = self.Power(base, exponent>>1)
        result *= result
        if exponent & 1 ==1:
            result *= base

        return result

    
S = WithExponent()
print(S.Power(0, -2))
print(S.Power(2, -2))
