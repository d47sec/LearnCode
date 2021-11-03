class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        result = [0] * (rowIndex+1)
        result[0] = [1]
        result[1] = [1,1]
        for i in range(2, rowIndex+1):
            temp = [0] * (i+1)
            for j in range(0, i+1):
                if j == 0 or j == i:
                    temp[j] = 1
                else:
                    temp[j] = result[i-1][j-1] + result[i-1][j]
            result[i] = temp
        return result[rowIndex]