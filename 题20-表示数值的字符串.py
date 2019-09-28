"""
题20-表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串 "+100", "5e2", "-123", "3.1416" 和 "-1E-16" 都表示数值。 
但是 "12e", "1a3.14", "1.2.3", "+-5" 和 "12e+4.3" 都不是。
"""

class Solution:

    # float强转
    def floatNumeric(self, s):
        try:
            if float(s):
                return True
            else:
                return False
        except:
            return False

    # 使用正则表达式
    def reNumeric(self, s):
        if not s:
            return False

        # 正则表达式，*匹配前一个字符出现无限次或0次，？匹配前一个字符出现一次或0次，+匹配前一个字符出现1次
        # 或无限次，.表示小数点已经转义了
        elif re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s):
            return True

        else:
            return False


s = Solution()
print(s.floatNumeric('1.2.3'))
print(s.reNumeric('1.2.3'))
