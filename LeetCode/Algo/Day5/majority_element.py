class Solution:
    def majorityElement(self, nums) -> int:
        # SOLUTION 1: HASH-MAP 
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        max_e = 0
        for i in dic:
            if dic[i] > max_e:
                max_e = dic[i]
        for i in dic:
            if dic[i] == max_e:
                return i 
        
        # SOLUTION 2 : Boyer-Moore Voting Algorithm
        # JAVA
        # class Solution {
        #     public int majorityElement(int[] nums) {
        #         int count = 0;
        #         Integer candidate = null;

        #         for (int num : nums) {
        #             if (count == 0) {
        #                 candidate = num;
        #             }
        #             count += (num == candidate) ? 1 : -1;
        #         }

        #         return candidate;
        #     }
        # }
        # PYTHON3
        # class Solution:
        # def majorityElement(self, nums):
        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)

        # return candidate
nums = [2,2,1,1,1,2,2]
solve = Solution()
print(solve.majorityElement(nums))
# Output: 3

# https://leetcode.com/problems/majority-element/
