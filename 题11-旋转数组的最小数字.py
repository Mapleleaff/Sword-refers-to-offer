def minnuminrotatearray(array):
    if len(array) == 0:
        return 0
    first, last = 0, len(array)-1
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
