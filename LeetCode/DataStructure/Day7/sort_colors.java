class Solution {
    public int[] sortColors(int[] nums) {
        int r=0, w=0, b=0;
        for(int num: nums){
            if(num == 0)
                r++;
            else if(num==1)
                w++;
            else
                b++;
        }
        for(int i=0; i < r; i++){
            nums[i] = 0;
        }
        for(int i=0; i < w; i++){
            nums[r+i] = 1;
        }
        for(int i=0; i < b; i++){
            nums[r+w+i] = 2;
        }
        return nums;
    }
    public static void main(String[] args) {
        int[] array = {2,0,2,1,1,0};
        Solution solve = new Solution();
        array = solve.sortColors(array);
        for(int i : array){
            System.out.print(i + " ");
        }
    }

}