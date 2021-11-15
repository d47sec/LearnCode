class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = ''
        carry = 0 
      
        
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0 
            
            result = ('1' if r % 2 == 1 else '0') + result
            
            carry = 0 if r < 2 else 1 
            
        if carry != 0 : result = '1' + result
        return result 
        
            
solve = Solution()
print(solve.addBinary("1", "1"))

# Đề bài: cho 2 chuỗi binary yêu cầu cộng 2 chuỗi đó lại với nhau 
# Hàm zfill(width) nó sẽ padding 0 vào phía bên trái cho đến khi chuỗi đó có độ dài bằng width
