class WithExponent:
    def Power(self, base, exponent):
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
print(S.Power(2, -2))
