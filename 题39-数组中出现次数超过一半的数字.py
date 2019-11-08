"""
题39-数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为 9 的数组 {1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了 5 次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

class Solution:
    def Check(self, arr, length, number):
        times = 0
        for i in range(length):
            if arr[i] == number:
                times += 1
        if times*2 <= length:
            return False
        return True

    def MoreThanHalfNum(self, arr):
        if len(arr) <= 0:
            return None

        num = arr[0]
        count = 1
        for i in range(1, len(arr[1:])):
            if arr[i] == arr[i-1]:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = arr[i]
                count = 1

        if not self.Check(arr, len(arr), num):
            num = 0
        return num


S = Solution()
print(S.MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum([1, 2]))
print(S.MoreThanHalfNum([1]))
print(S.MoreThanHalfNum([]))
