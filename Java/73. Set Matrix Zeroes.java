class Solution {
    public void setZeroes(int[][] matrix) {
        if(matrix==null || matrix.length == 0) return;
        boolean firstRow = false;
        boolean firstCol = false;
        // iterate first row 
        for(int j=0; j<matrix[0].length; j++){
            if(matrix[0][j]==0){
                firstRow=true;
                break; 
            }        
        }
        // iterate first col
        for(int i=0; i<matrix.length; i++){
            if(matrix[i][0]==0){
                firstCol=true;
                break;
            }
        }        
        // iterate through rest of matrix and mark first row and first col
        for(int i=1; i<matrix.length; i++){
            for(int j=1;j<matrix[0].length;j++){
                if(matrix[i][j]==0){
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
        }
        // iterate through first row
        for(int j=1; j<matrix[0].length; j++){
            if(matrix[0][j]==0){
                for(int i=1; i<matrix.length;i++){matrix[i][j]=0;}
            }
        }
        // iterate through first col
        for(int i=1; i<matrix.length;i++){
            if(matrix[i][0]==0){
                for(int j=1; j<matrix[0].length;j++){matrix[i][j]=0;}
            }
        }
        if(firstRow) for(int j=0; j<matrix[0].length;j++) matrix[0][j]=0;
        if(firstCol) for(int i=0; i<matrix.length; i++) matrix[i][0]=0;
        return;
    }    
}