class Solution {
    public int mySqrt(int n) {
        if(n<=0) return 0;   
        int magicNum = (int) Math.sqrt(Integer.MAX_VALUE);
        int start=1, end = magicNum;
        while(start+1<end){
            int mid = start + (end-start)/2;
            if(mid*mid==n) return mid;
            if(mid*mid>n) end = mid;
            else start = mid;
        }
        if(end*end<=n) return end;
        else return start;
        /* does not work for corner case
        int curr = 0;
        int add = 1;
        int res = 0;        
        while(curr<=n){
            if(add + curr > Integer.MAX_VALUE) return res;
            curr += add;
            res ++;
            add +=2;
        }
        return res-1;  
        */
    }
}