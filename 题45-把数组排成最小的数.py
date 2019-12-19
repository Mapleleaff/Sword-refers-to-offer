"""
题45-把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组 {3，32，321}，则打印出这三个数字能排成的最小数字为 321323。
"""

from functools import cmp_to_key

class Solution:
    def GetMinNumber(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return []
        strList = [str(i) for i in numbers]
        key = cmp_to_key(lambda x, y: int(x+y)-int(y+x))
        strList.sort(key=key)

        return ''.join(strList)


    # 使用冒泡排序
    def GetMinNumber2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return []
        strNum = [str(i) for i in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]

        return ''.join(strNum)


numbers = [3, 32, 321]
S = Solution()
print(S.GetMinNumber(numbers))
print(S.GetMinNumber2(numbers))
