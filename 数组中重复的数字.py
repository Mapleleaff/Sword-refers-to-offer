

def duplicate(x,dup=[]):
    m = len(x)
    for i in range(m):
        while x[i] != i:
            index = x[i]
            if x[i] == x[index]:
                dup.append(x[i])
                return True,dup
            else:
                x[i], x[index] = x[index], x[i]
    return False, dup
test = [2, 3, 1, 0, 2, 5, 3]
s, dup = duplicate(test,[])
print("{},{}".format(s,dup))