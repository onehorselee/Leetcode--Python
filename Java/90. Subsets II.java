public class Solution{
    public List<List<Integer>> subsetsWithDup(int[] nums){
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0) return result;
        Arrays.sort(nums);
        BinarybacktrackingHelper(nums, 0, true, result, new ArrayList<Integer>());
        return result;
    }
   
    public void BinarybacktrackingHelper(int[] nums, int currIdx, boolean taken, List<List<Integer>> result, ArrayList<Integer> curr){
        if(currIdx==nums.length) result.add(new ArrayList<Integer>(curr));
        else{
            // skip current idx number
            BinarybacktrackingHelper(nums, currIdx+1, false, result, curr);
            // add current idx number
            if(taken || nums[currIdx-1] != nums[currIdx]){
                curr.add(nums[currIdx]);
                BinarybacktrackingHelper(nums, currIdx+1, true, result, curr);
                curr.remove(curr.size()-1);
            }            
        }
    }
}