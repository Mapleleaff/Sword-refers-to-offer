"""
题5-替换空格
请实现一个函数，将一个字符串中的空格替换成 "%20"。
例如，当字符串为 "We Are Happy". 则经过替换之后的字符串为 "We%20Are%20Happy"
"""

# 普通方法
class Solution:
    def replaceSpace(self, s):  
        if s == None:
            return None
        if len(s) == 0:
            return ''
        result = ''
        for item in s:
            if item.isspace():
                result = result+'%20'
            else:
                result = result+item
        return result

    
# 先遍历，再逆向扫描替换方法
def respace(s):
    count = 0
    for i in s:
        if i == ' ':
            count += 1
    if count == 0:
        return s
    newlen = len(s) + count*2
    newstr = [None] * newlen
    index = len(s) -1
    jn = newlen - 1
    while index >= 0 :
        if s[index] == " ":
            newstr[jn-2:jn+1] = ['%','2','0']
            index -= 1
            jn -= 3
        else:
            newstr[jn] = s[index]
            index -= 1
            jn -= 1
        print(newstr)
    return ''.join(newstr)


s = 'we are happy.'
print(respace(s))
