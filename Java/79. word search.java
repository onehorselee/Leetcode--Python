class Solution {
    public boolean exist(char[][] board, String word) {
        // backtracking
        if(board==null) return false;
        boolean[][] used = new boolean[board.length][board[0].length];
        for(int row=0; row<board.length; row++){
            for(int col=0; col<board[0].length; col++){
                if(existHelper(board, used, word.toCharArray(), 0, row, col)){
                    return true;
                }
            }
        }
        return false;        
    }

    public boolean existHelper(char[][] board, boolean[][] used, char[] word, int idx, int row, int col){
        if(idx==word.length) return true;
        if(row<0 || row>=board.length || col<0 || col>=board[0].length) return false;
        if(used[row][col]==true || board[row][col]!=word[idx]) return false;
        
        used[row][col]=true;
        boolean exist = existHelper(board, used, word, idx+1, row+1, col);
        if(exist) return true;
        exist = existHelper(board, used, word, idx+1, row-1, col);
        if(exist) return true;
        exist = existHelper(board, used, word, idx+1, row, col+1);
        if(exist) return true;
        exist = existHelper(board, used, word, idx+1, row, col-1);
        if(exist) return true;
        // if all four directions did not find a one - go back one step
        used[row][col]=false;
        return false;
    }
}