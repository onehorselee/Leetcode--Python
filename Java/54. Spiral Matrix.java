class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {        
        List res = new ArrayList<>();
        if(matrix==null || matrix.length==0 || matrix[0].length==0) return res;
        int n_rows = matrix.length-1, n_cols = matrix[0].length-1;
        int left = 0, right = n_cols;
        int top = 0, bottom = n_rows;
        while(left<right && top < bottom){
            for(int i=left; i<right; i++) res.add(matrix[top][i]);
            for(int i=top; i<bottom; i++) res.add(matrix[i][right]);
            for(int i=right; i>left; i--) res.add(matrix[bottom][i]);
            for(int i=bottom; i>top; i--) res.add(matrix[i][left]);
            left++;
            right--;
            top++;
            bottom--;            
        }
        if(left == right){
                for(int i=top; i<=bottom; i++) res.add(matrix[i][left]); 
        }else if(top == bottom){
                for(int i=left; i<=right; i++) res.add(matrix[top][i]);            
        } 
        return res;        
    }
}