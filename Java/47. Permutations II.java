// [1,1,2,1] with duplicates
// backtracking

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) { 
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0) return res;
        helper(nums, new ArrayList<Integer>(), res, new boolean[nums.length]);
        return res;       
    }
    
    public void helper(int[] nums, List<Integer> curList, List<List<Integer>> res, boolean[] used){
        if(curList.size()==nums.length) res.add(new ArrayList<Integer>(curList));
        else{
            int preNum = nums[0]-1;
            for(int i=0; i<nums.length; i++){
                if((used[i]==false) && (preNum != nums[i])){
                    preNum = nums[i];
                    curList.add(nums[i]);
                    //int lastIx = curList.size()-1;
                    used[i] = true;
                    helper(nums, curList, res, used);
                    used[i] = false;
                    curList.remove(curList.size()-1);
                }
            }
        }
    }
}