// no duplicates in candidates
// one candidates can be used unlimited times
// ref: http://www.goodtecher.com/leetcode-39-combination-sum/
class Solution {
  public List<List<Integer>> combinationSum(int[] candidates, int target) {
      List<List<Integer>> results = new ArrayList<>();  
      
      if (candidates == null || candidates.length == 0) {
          return results;
      }        
      
      Arrays.sort(candidates);    
      
      List<Integer> combination = new ArrayList<>();
      toFindCombinationsToTarget(candidates, results, combination, 0, target);   
      
      return results;
  }
  
  private void toFindCombinationsToTarget(int[] candidates, List<List<Integer>> results, List<Integer> combination, int startIndex, int target) {
      if (target == 0) {
          results.add(new ArrayList<>(combination));
          return;
      }
      
      for (int i = startIndex; i < candidates.length; i++) {
          if (candidates[i] > target) {
              break;
          }    
          
          combination.add(candidates[i]);
          toFindCombinationsToTarget(candidates, results, combination, i, target - candidates[i]);
          combination.remove(combination.size()-1);
      }        
  }
}

