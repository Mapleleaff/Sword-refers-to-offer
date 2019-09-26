"""
题21-调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分
"""

class Solution(object):
    # 两列表解法
    def orderList(self, array):
        odd, even = [], []
        for i in array:
            if self.isEvein(i):
                even.append(i)
            else:
                odd.append(i)
        return odd + even

    # 冒泡思想解法
    def orderArray(self, array):
        for i in range(len(array)-1, -1, -1):
            for j in range(i):
                if (array[j] % 2 == 0) and (array[j+1] % 2 == 1):
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    # 扩展性能解法
    def ReorderOddEven(self, array):
        length = len(array)
        return self.Reorder(array,length, func = self.isEvein)

    def Reorder(self, array, length, func):
        if length == 0:
            return
        begin, end = 0, length -1
        while begin < end:
            while begin < end and not func(array[begin]):
                begin +=1
            while begin <end and func(array[end]):
                end -= 1

            if begin < end:
                array[begin], array[end] = array[end], array[begin]
        return array

    def isEvein(self, n):
        return not n & 1

    def isNegtive(self, n):
        return n >=0


S = Solution()
print(S.orderList([1,2,3,4,5,6,7,8,9,]))
print(S.orderArray([1,2,3,4,5,6,7,8,9,]))
print(S.ReorderOddEven([1,2,3,4,5,6,7,8,9]))
print(S.ReorderOddEven([-1,2,-3,4,5,-6,-7]))
