// traditional backtracking
public class Solution{
    public List<List<Integer>> subsets(int[] nums){
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0) return result;
        backtrackingHelper(nums, 0, result, new ArrayList<Integer>());
        return result;

    }
    public void backtrackingHelper(int[] nums, int currIdx, List<List<Integer>> result, List<Integer> curr){
        result.add(new ArrayList<Integer>(curr));
        for(int idx=currIdx; idx<nums.length; idx++){
            curr.add(nums[idx]);
            backtrackingHelper(nums, idx+1, result, curr);
            curr.remove(curr.size()-1);
        }
    }
} 


// binary choice -  backtracking
public class Solution{
    public List<List<Integer>> subsets(int[] nums){
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0) return result;
        BinarybacktrackingHelper(nums, 0, result, new ArrayList<Integer>());
        return result;
    }
   
    public void BinarybacktrackingHelper(int[] nums, int currIdx, List<List<Integer>> result, ArrayList<Integer> curr){
        if(currIdx==nums.length) result.add(new ArrayList<Integer>(curr));
        else{
            // skip current idx number
            BinarybacktrackingHelper(nums, currIdx+1, result, curr);
            // add current idx number
            curr.add(nums[currIdx]);
            BinarybacktrackingHelper(nums, currIdx+1, result, curr);
            curr.remove(curr.size()-1);
        }
    }
}