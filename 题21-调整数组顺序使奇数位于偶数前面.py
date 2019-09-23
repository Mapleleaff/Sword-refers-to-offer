class Solution(object):
    def orderArray(self, array):
        for i in range(len(array)-1, -1, -1):
            for j in range(i):
                if (array[j] % 2 == 0) and (array[j+1] % 2 == 1):
                    array[j], array[j+1] = array[j+1], array[j]
        return array

S = Solution()
print(S.orderArray([1,2,3,4,5,6,7,8,9,10,11,12,13]))
