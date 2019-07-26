class Solution {
    public int[] plusOne(int[] digits) {
        if(digits==null  || digits.length==0) return new int[0];
        
        for(int i=digits.length-1; i>=0; i--){
            if(digits[i]<9){
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        int[] new_digits = new int[digits.length+1];
        System.arraycopy(digits, 0, new_digits, 1, digits.length);
        new_digits[0]=1;
        return new_digits;
    }
}