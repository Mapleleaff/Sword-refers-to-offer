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
