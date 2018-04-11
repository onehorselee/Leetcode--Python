from collections import defaultdict
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        len_word = len(words[0])
        len_combo = len_word * len(words)
        if len(s) < len_combo:
            return []
        
        result = []
        dic = {w:words.count(w) for w in words}
        # search words combinations in s
        for i in range(len(s) - len_combo + 1):
            seen = defaultdict(int)
            start, count = i, len(words)
            while count > 0:
                substr = s[start: start + len_word]
                # it is not in words list or it has more than the number of words
                if (substr not in dic) or (dic[substr] == seen[substr]):  
                    break
                else:
                    seen[substr] += 1
                    start += len_word
                    count -= 1
            
            if count == 0:
                result.append(i)            
    
        return result
