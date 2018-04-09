class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 1)  recursive
        '''
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(dic[digits[0]])

        pre = self.letterCombinations(digits[:-1])
        cur = dic[digits[-1]]
        
        return [i + j for i in pre for j in cur]        
        
        '''
        
        # 2) interation
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if digits:
            res = ['']
        else:
            return []
        
        for d in digits:
            d_list = list(dic[d])
            temp = []
            for i in d_list:
                for j in res:
                    temp.append(j + i)
            res = temp
         # it equals to one statement......
         #ans = [i + j for j in dic[d] for i in res]

        return res

