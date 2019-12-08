"""
题41-数据流中的中位数
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
"""

import heapq

class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, numlist):
        for num in numlist:
            if self.count & 1 == 0:
                self.left.append(num)
            else:
                self.right.append(num)
            self.count += 1

    def GetMedian(self):
        if self.count == 1:
            return self.left[0]

        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)

        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2
        else:
            return self.left[0]


    def GetMedian_v2(self):
        if self.count == 1:
            return self.left[0]

        left = heapq.nlargest(len(self.left), self.left)
        leftmax = left[0]
        right = heapq.nsmallest(len(self.right), self.right)
        rightmin = right[0]

        if leftmax > rightmin:
            left[0], right[0] = right[0], left[0]

        left = heapq.nlargest(len(left), left)
        right = heapq.nsmallest(len(right), right)

        if self.count & 1 == 0:
            return (left[0] + right[0]) / 2
        else:
            return left[0]


    def MaxHeap(self, array):
        length = len(array)
        if array == None or length <= 0:
            return []
        if length == 1:
            return array
        for i in range(length//2-1, -1, -1):
            k = i
            temp = array[k]
            heap = False
            while not heap and 2*k < length-1:
                index = 2*k+1
                if index < length - 1:
                    if array[index] < array[index+1]:
                        index += 1
                if temp >= array[index]:
                    heap = True
                else:
                    array[k] = array[index]
                    k = index
            array[k] = temp

    def MinHeap(self, array):
        length = len(array)
        if array == None or length <= 0:
            return []
        if length == 1:
            return array
        for i in range(length//2-1, -1, -1):
            k = i
            temp = array[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if array[index] > array[index + 1]:
                        index += 1
                if temp <= array[index]:
                    heap = True
                else:
                    array[k] = array[index]
                    k = index
            array[k] = temp


array = [2,4,5,7,11,99,14,13,19]
S = Solution()
for i in array:
    S.Insert([i])
    print(S.GetMedian())
    print(S.GetMedian_v2())


