// [1,2,3], with distinct numbers
// backtracking 
class Solution {
    public List<List<Integer>> permute(int[] nums) {        
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        helper(nums, new ArrayList<Integer>(), res, new HashSet<Integer>());
        return res;       
    }
    
    public void helper(int[] nums, List<Integer> curList, List<List<Integer>> res, HashSet<Integer> set){
        if(curList.size()==nums.length) res.add(new ArrayList<Integer>(curList));
        else{
            for(int i=0; i<nums.length; i++){
                if(!set.contains(nums[i])){
                    curList.add(nums[i]);
                    int lastIx = curList.size()-1;
                    set.add(nums[i]);
                    helper(nums, curList, res, set);
                    set.remove(nums[i]);
                    curList.remove(lastIx);
                }
            }
        }
    }
}