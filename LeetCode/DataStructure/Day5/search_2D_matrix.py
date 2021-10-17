class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 2D => 1D
        cols = len(matrix[0])
        rows = len(matrix)
        result = [0] * (cols*rows)
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                result[r*cols+c] = matrix[r][c]
        print(result)
        # two pointers 
        left, right = 0, len(result)-1 
        while left <= right:
            mid = (left + right) // 2
            if result[mid] == target:
                return True
            elif result[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 33
solve = Solution()
print(solve.searchMatrix(matrix, target))