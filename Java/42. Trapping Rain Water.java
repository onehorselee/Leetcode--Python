class Solution {
    public int trap(int[] height) {
        
        if(height==null || height.length<3) return 0;
        int res=0;
        int leftmax = 0;
        int rightmax = 0;
        int i=0;
        int j = height.length-1;
        while(i<j){
            leftmax = Math.max(leftmax, height[i]);
            rightmax = Math.max(rightmax, height[j]);
            if(leftmax < rightmax){
                res += leftmax - height[i];
                i++;
            }else{
                res += rightmax - height[j];
                j--;
            }
        }
        return res;        
    }
}