class Solution {
    public int maxSubArray(int[] nums) {

        int maxCurr = nums[0]
        int maxRes = nums[0]
        for(int i=0; i< nums.length;i++){
            maxCurr = Math.max(maxCurr, maxCurr+nums[i]);
            maxRes = Math.max(maxCurr, maxRes);
        }
        return maxRes;        
    }
}