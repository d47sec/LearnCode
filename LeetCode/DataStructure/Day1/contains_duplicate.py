class Solution:
    # Cách 1 : Sài set trong python 
    # def containsDuplicate(self, nums) -> bool:
    #     return True if len(nums) != len(set(nums)) else False
    
    # Cách 2: Sài dictionary
    # tốc độ nhanh hơn 
    def containsDuplicate(self, nums)->bool:
        dic = {}
        for i in nums:
            if i not in dic:
                return True
            dic[i] = 1
        return False
    
nums = [1,1,1,3,3,4,3,2,4,2]
solve = Solution()
print(solve.containsDuplicate(nums))