class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        
        min_len = min([len(s) for s in strs])        
        strs = [s[:min_len] for s in strs]
        
        res = strs[0]        
        for i in range(1, len(strs)):
            while len(res) != 0:
                if res != strs[i][:len(res)]:
                    res = res[:-1]                    
                else:
                    break
                    
        return res
            
