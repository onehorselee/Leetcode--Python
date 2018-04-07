class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1) count the frequency of chars
        dic = {}
        for i, char in enumerate(s):
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        # 2) calculate the length
        odd, leng = False, 0
        for char in dic:
            if dic[char] >= 2:                
                leng += (dic[char] //2)  * 2
                dic[char] = dic[char] % 2
                if dic[char] == 1:
                    odd = True
            else:
                odd = True
         
        return leng + 1 if odd else leng
