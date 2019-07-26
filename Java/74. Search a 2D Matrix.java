class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int startRow = 0;
        int endRow = matrix.length -1;
        int endCol = matrix[0].length - 1;
        int row = -1;
        while(startRow + 1 < endRow){
            int midRow = startRow + (endRow - startRow)/2;
            if(matrix[midRow][endCol]<target) startRow = midRow;
            else endRow = midRow;
        }
        // the order matters here
        if(matrix[startRow][endCol]>= target) row = startRow;
        else if(matrix[endRow][endCol]>= target) row = endRow;
        else return false;
        
        int start = 0;
        int end = endCol;
        while(start+1 < end){
            int mid = start + (end-start)/2;
            if(matrix[row][mid] < target) start = mid;
            else end = mid;
        }        
        if(matrix[row][start]==target||matrix[row][end]==target) return true;
        else return false;        
    }
}