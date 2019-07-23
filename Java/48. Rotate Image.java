class Solution {
    public void rotate(int[][] matrix) {
        if(matrix == null || matrix.length==0 || matrix[0].length==0) return;
        int n = matrix.length-1;
        int top=0; int left=0;
        int right = n;  int bottom = n;
        while(n>=1){
            for(int i=0;i<n;i++){
                int tmp = matrix[top+i][left];
                matrix[top+i][left] = matrix[bottom][left+i]; //1
                matrix[bottom][left+i]= matrix[bottom-i][right];//2
                matrix[bottom-i][right] = matrix[top][right-i]; //3
                matrix[top][right-i] = tmp; //4                
            }
            top++;
            bottom--;
            left++;
            right--;
            n-=2;
        }        
    }
}