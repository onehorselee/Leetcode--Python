// o(n2) solution
class Solution {
    public int largestRectangleArea(int[] heights) {
        if(heights==null || heights.length==0) return 0;
        int max=0;
        for(int curr=0; curr < heights.length; curr++){
            if(curr == heights.length-1 || heights[curr] > heights[curr+1]){
                int miniHeight = heights[curr];
                for(int idx=curr; idx >= 0; idx--){
                    miniHeight = Math.min(miniHeight, heights[idx]);
                    max = Math.max(max, miniHeight * (curr-idx +1));
                }
            }
        }
        return max;        
    }
}

// stack o(n) solution
class Solution {
    public int largestRectangleArea(int[] heights) {
        if(heights == null || heights.length == 0) return 0;
        int max=0;
        Stack<Integer> stack = new Stack<Integer>();
        for(int curr = 0; curr < heights.length; curr++){
            if(stack.isEmpty() || heights[curr] >= heights[stack.peek()]){
                stack.push(curr);
            }else{
                int right = curr;
                int index = stack.pop();
                while(!stack.isEmpty() && heights[index] == heights[stack.peek()]){
                    index = stack.pop();
                }
                int leftMost = (stack.isEmpty())? -1: stack.peek();
                max = Math.max(max, (right-leftMost-1) * heights[index]);
                curr--;
            }
        }
        int rightMost = stack.peek()+1;
        while(!stack.isEmpty()){
            int index = stack.pop();
            int left = (stack.isEmpty())? -1: stack.peek();
            max = Math.max(max, (rightMost-left-1)*heights[index]);
        }
      return max;
    }
}