"""
题21-调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分
"""

class Solution(object):
    def orderArray(self, array):
        for i in range(len(array)-1, -1, -1):
            for j in range(i):
                if (array[j] % 2 == 0) and (array[j+1] % 2 == 1):
                    array[j], array[j+1] = array[j+1], array[j]
        return array

S = Solution()
print(S.orderArray([1,2,3,4,5,6,7,8,9,10,11,12,13]))
