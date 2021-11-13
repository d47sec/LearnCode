class Solution:
    def findDiagonalOrder(self, mat):
        
        dic = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in dic:
                    dic[i+j] = [mat[i][j]]
                else:
                    dic[i+j].append(mat[i][j])
        
        # print(dic)
        
        ans = []
        for entry in dic.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
    

mat = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
solve = Solution()
print(solve.findDiagonalOrder(mat))
    
# IDEA: https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
        
# https://leetcode.com/problems/diagonal-traverse/

# ý tưởng đây là gì ???
# Những hàng chéo nhau trong ma trận thì có tổng index của hàng và cột là bằng nhau 

# a[0][0]  a[0][1] a[0][2]
# a[1][0]  a[1][1] a[1][2]
# a[2][0]  a[2][1] a[2][2]

# +) Sau đó sài dictionary (hash table) gom những thằng có index hàng + cột bằng nhau vào một mảng 
# +) Trong dic đó, thằng nào có key chẵn thì cần phải reverse cái mảng đó để chạy đúng nữa là xong 