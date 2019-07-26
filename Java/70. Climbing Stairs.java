class Solution {
    public int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;
        int curr = 2;
        int prev = 1;
        for(int i=3; i<=n; i++){
            curr = curr + prev;
            prev = curr - prev;
        }
        return curr;        
    }
}