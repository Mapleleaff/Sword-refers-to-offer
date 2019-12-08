"""
题42-连续子数组的最大和
输入一个整型数组，数组里有整数也有负数。
数组中一个或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
"""

class Solution:
    def findmaxsumofsubarray(self, array):
        if array == None or len(array) <= 0:
            return 0

        maxsum, subsum = array[0],0
        for num in array:
            if subsum < 0:
                subsum = num
            else:
                subsum += num

            if subsum > maxsum:
                maxsum = subsum

        return maxsum


    # 动态规划实现
    def findmaxsumofsubarray_v2(self, array):
        if array == None or len(array) <= 0:
            return 0

        maxsum_list = [0] * len(array)
        for index, num in enumerate(array):
            if index == 0 or maxsum_list[index-1] < 0:
                maxsum_list[index] = num
            else:
                maxsum_list[index] = maxsum_list[index-1] + num

        return max(maxsum_list)


array = [2,-4,5,-3,11,-14]
S = Solution()
print(S.findmaxsumofsubarray(array))
print(S.findmaxsumofsubarray_v2(array))
