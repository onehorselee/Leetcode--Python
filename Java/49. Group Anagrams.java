class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        ArrayList<List<String>> results = new ArrayList<>();
        if(strs==null || strs.length==0) return results;
        HashMap<String, List<String>> map = new HashMap();
        for(int i=0; i< strs.length; i++){
            char[] curr = strs[i].toCharArray();
            Arrays.sort(curr);
            String key = String.valueOf(curr);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(strs[i]);
        }
        return new ArrayList<List<String>>(map.values());
    }
}