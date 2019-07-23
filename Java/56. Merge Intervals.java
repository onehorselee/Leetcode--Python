//Given a collection of intervals, merge all overlapping intervals.

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<int[]>();
        if(intervals==null) return new int[0][0];
        int[] start = new int[intervals.length];
        int[] end = new int[intervals.length];
        for(int i=0; i< intervals.length; i++){
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }        
        Arrays.sort(start);
        Arrays.sort(end);        
        int i=0, ix=0;
        while(i<intervals.length){
            int st = start[i];
            while(i<intervals.length-1 && start[i+1] <= end[i]) i++;
            int ed = end[i];
            int[] intv = new int[2];
            intv[0] = st;
            intv[1] = ed;
            res.add(intv);
            i++;
        }
        // convert Arraylist to int[][]
        int[][] output = new int[res.size()][];
        for(int j=0; j< res.size(); j++){
            output[j] = res.get(j);
        }
        return output;
    }
}