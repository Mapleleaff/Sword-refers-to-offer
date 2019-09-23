"""
题4-二维数组中的查找
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

def findnum(mat, num):
    if mat == None:
        return False
    
    n = len(mat)-1
    m = len(mat[0])-1
    i = 0
    while (i <= m) and (n >= 0):
        if mat[n][i] < num:
            i += 1
        elif mat[n][i] > num:
            n -= 1
        else:
            return True
    return False


mat = [[1, 2, 8, 9],
        [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
for num in range(30):
    print(findnum(mat,num))
