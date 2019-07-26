class Solution {
    public String simplifyPath(String path) {
        if(path.length()<=1) return path;
        String[] splitted = path.split("/");
        Stack<String> stack = new Stack<>();
        for(String ele: splitted){
            if(ele.equals("..")){
                if(!stack.isEmpty()) stack.pop();
            }else{
                if(!ele.equals(".") && !ele.isEmpty()) stack.push(ele);
            }
        }
        
        String results = "";
        if(stack.isEmpty()) return "/";
        while(!stack.isEmpty()){
            String newPop = stack.pop();
            results = "/" + newPop + results;
        }
        return results;        
    }
}