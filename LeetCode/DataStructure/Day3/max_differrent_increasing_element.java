class Solution {
    public int maximumDifference(int[] nums) {
        int max_diff = -1;
        int temp1 = nums[0];
        int max;
        for(int i = 1; i < nums.length; i++){
            max = nums[i] - temp1;
            if(max > max_diff && max != 0){
                max_diff = max;
            }
            if(temp1 > nums[i]){
                temp1 = nums[i];
            }
        }
        return max_diff;
    }
}

// LOL faster 100% java submissions