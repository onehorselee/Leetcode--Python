class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ''' 
        # 1) Interation
        result = [nums]
        for i in range(len(nums)-1):
            for one in result[:]:
                for j in range(i+1, len(nums)):
                    result.append(one[:i] + one[j:] + one[i:j])
        return result      
        '''
        
        #  2) backtracking
        res = []        
        def helper(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                helper(nums, temp)
                temp.pop()
                
        helper(nums,[])
        return res
    
    
    # 3) dynamic programming
        def insert_num(temp, num):
            if temp == []:
                temp.append([num])
                return temp

            res = []
            for i in temp:
                for j in range(len(i) + 1):
                    i_copy = list(i)
                    i_copy.insert(j, num)
                    res.append(i_copy)
            return res

        temp = []
        for i in nums:
            temp = insert_num(temp, i)
            
        return temp
