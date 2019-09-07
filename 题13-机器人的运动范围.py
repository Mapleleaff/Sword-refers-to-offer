import numpy as np

class Solution():
    def hasPath(self, rows, cols, threshold):
        if threshold < 0 or rows < 1 or cols < 1:
            return 0

        visited = np.zeros((rows, cols))
        i, j = 0, 0
        count = self.hasPathCore(i,j,rows,cols,threshold,visited)
        return count

    def hasPathCore(self,i,j,rows,cols,threshold,visited):
        count = 0
        if i<rows and i>=0 and j<cols and j>=0 and visited[i][j]==0 and self.check(i,j)<=threshold:
            visited[i][j] = 1
            count = 1 + self.hasPathCore(i-1, j, rows, cols, threshold, visited) \
                      + self.hasPathCore(i+1, j, rows, cols, threshold, visited) \
                      + self.hasPathCore(i, j-1, rows, cols, threshold, visited) \
                      + self.hasPathCore(i, j+1, rows, cols, threshold, visited)
        return count

    def check(self,i,j):
        sum = 0
        while i>0 or j>0:
            if i>0:
                sum = sum + i % 10
                i = i//10
            if j>0:
                sum = sum + j % 10
                j = j // 10
        return sum


a = 2
b = 3
c = 1
s = Solution()
print(s.hasPath( a, b, c))
