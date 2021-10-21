import java.util.Scanner;
class Solution {
    public int climbStairs(int n) {
        if(n==1) return 1;
        if(n==0) return 0;
        int pre = 1;
        int curr = 2;
        for(int i = 3; i <= n; i++){
            int sum = pre + curr;
            pre = curr;
            curr = sum;
        }
        return curr;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Solution solve = new Solution();
        System.out.println(solve.climbStairs(n));
    }
}