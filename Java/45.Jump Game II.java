public class Solution{
    // solution 1
    public int jump(int[] nums){
        if(nums==null || nums.length <=1) return 0；
        int currMax = 0;
        int nexMax = 0;
        int step = 0;
        int index = 0;
        while(index <= currMax){
            while (index <= currMax){
                naxtMax = Math.max(nextMax, index + nums[index]);
                index ++;
            }
            currMax = nextMax;
            step++;
            if(currMax >= nums.length-1) return step;
        }
        return 0;
    }

    // solution 2
    public int jump2(int[] nums) {
        int times = 0;
        int reached = 0;
        int max = 0;
        for(int i=0;i< nums.length;i++){
            if(reached < i){
                times++;
                reached = max;
            }
            max = Math.max(max,i+nums[i]);
        }
        return times;
    }
}