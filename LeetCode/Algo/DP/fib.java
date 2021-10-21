import java.util.Scanner;
class Solution {
    public long fib(int n) {
       long pre = 1; //  f1 = 1
       long curr = 1; // f2 = 1
       for(int i = 3; i <= n; i++){
           long result = pre + curr;
           pre = curr;
           curr = result;
       }
       return curr;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Solution solve = new Solution();
        System.out.println(solve.fib(n));
    }
}
// 1 1 2 3 5