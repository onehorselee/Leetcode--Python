class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        if(n<=0 || k<= 0) return results;
        combinationHelp(n, k, 1, results, new ArrayList<>());
        return results;        
    }
    
    public void combinationHelp(int n, int k, int start_num, List<List<Integer>> results, ArrayList<Integer> curSeq){
        if(k==0) results.add(new ArrayList<Integer>(curSeq));
        else{
            for(int i = start_num; i<=n; i++){
                curSeq.add(i);
                combinationHelp(n, k-1, i+1, results, curSeq);
                curSeq.remove(curSeq.size()-1);
            }
        }
    }
}