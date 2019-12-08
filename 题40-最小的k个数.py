"""
题40-最小的 k 个数围
输入 n 个整数，找出其中最小的 k 个数。例如，输入
4、5、1、6、2、7、3、8 这些数字，则最小的 4 个数字是1、2、3、4
"""

import heapq

class Solution:

    # 堆实现
    def GetLeastNum(self, array, k):
        if array == None or len(array) < k or len(array) <= 0 or k <= 0:
            return []

        output = []
        for num in array:
            if len(output) < k:
                output += [num]
            else:
                output = heapq.nlargest(k, output)
                if num >= output[0]:
                    continue
                else:
                    output[0] = num

        return output[::-1]


    # 基于划分的方法
    def GetLeastNumofpartion(self, array, k):
        n = len(array)
        if k <= 0 or k > n:
            return []

        start, end = 0, n-1
        index = self.partion(array, start, end)
        while k-1 != index:
            if index < k-1:
                start = index + 1
            else:
                end = index - 1
            index = self.partion(array, start, end)
        res = array[:index + 1]
        res.sort()
        return res

    def partion(self, array, low, high):
        key = array[low]
        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] <= key:
                low += 1
            array[high] = array[low]
        array[low] = key
        return low


array = [3,1,5,4,2]
S = Solution()
print(S.GetLeastNum(array, 3))
print(S.GetLeastNumofpartion(array, 3))
