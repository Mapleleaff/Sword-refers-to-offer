"""
题3.2-不修改数组找出重复的数字
在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。
例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的输出是重复的数字2或者3。
"""

def countRange(numbers, length, start, middle):
    if numbers == []:
        return 0
    count = 0
    for i in range(0, length):
        if numbers[i] >= start and numbers[i] <= middle:
            count = count + 1
    return count


def duplicate( numbers, length):
    """ 长度为8的，所有数字在 1-7 """

    if numbers == []:
        return -1
    start = 1
    end = length - 1
    while start <= end:
        middle = (end - start) // 2 + start
        count = countRange(numbers, length, start, middle)
        print("start + end + middle + count:", start, end, middle, count)
        if (end == start):
            if count > 1:
                return start
            else:
                break
        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1


numbers = [2, 3, 1, 4, 6, 7, 2, 5]
length = 8
dup = duplicate(numbers, length)
print(dup)
