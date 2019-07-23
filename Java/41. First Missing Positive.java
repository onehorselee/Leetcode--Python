class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int missing = 1;
        int i = 0;        
        while(i < nums.length){
            if(nums[i] > missing){
                break;
            }else if(nums[i] < missing){
                i++;
            }else if(nums[i]==missing){
                missing++;
                i++;
            }
        }        
        return missing;        
    }
}