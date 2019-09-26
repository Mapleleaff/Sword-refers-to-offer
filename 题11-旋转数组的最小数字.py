"""
题11-旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组 {3,4,5,1,2} 为 {1,2,3,4,5} 的一个旋转，该数组的最小值为 1。
NOTE：给出的所有元素都大于 0，若数组大小为 0，请返回 0。
"""

def minnuminrotatearray(array):
    if len(array) == 0:
        return 0
    first, last = 0, len(array)-1
    if array[first]< array[last]:
        return array[first]
    
    while array[first] >= array[last]:
        if last-first == 1:
            return array[last]

        mid = (first + last)//2
        if array[mid] == array[first] == array[last]:
            result = array[0]
            for num in array[first:last+1]:
                if num< result:
                    result = num
            return result

        if array[mid] >= array[first]:
            first = mid

        elif array[mid] <= array[last]:
            last = mid

print(minnuminrotatearray([3, 4, 5, 1, 2]))
print(minnuminrotatearray([1, 2, 3, 4, 5]))
print(minnuminrotatearray([1, 1, 1, 0, 1]))
print(minnuminrotatearray([1, 0, 1, 1, 1]))
print(minnuminrotatearray([]))
print(minnuminrotatearray([1]))
