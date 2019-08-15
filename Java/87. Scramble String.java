class Solution {
    public boolean isScramble(String s1, String s2) {
    	if(s1==null || s2==null || s1.length() != s2.length()) return false;
    	if(s1.length()==1 && s1.equals(s2)) return true;
    	// check letters match
    	char[] s1char = s1.toCharArray();
    	char[] s2char = s2.toCharArray();
    	Arrays.sort(s1char);
    	Arrays.sort(s2char);
        String str1 = new String(s1char);
        String str2 = new String(s2char);
    	if(!str1.equals(str2)) return false;
    	// recursive
    	for(int length=1; length < s1.length();length++){
    		String s1left = s1.substring(0, length);
    		String s1right = s1.substring(length, s1.length());
            //
    		String s2left = s2.substring(0, length);
    		String s2right = s2.substring(length, s2.length());
            //
    		String s2left_2 = s2.substring(s2.length()-length, s2.length());
    		String s2right_2 = s2.substring(0, s2.length()-length);
    		if((isScramble(s1left, s2left) && isScramble(s1right, s2right)) ||
    			(isScramble(s1left, s2left_2) && isScramble(s1right, s2right_2))) return true;    		
    	}
    	return false;        
    }
}