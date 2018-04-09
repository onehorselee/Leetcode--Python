class Solution:
    def fourSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # edge
        if len(num) < 4:
            return []
        num.sort()
        
        twoSum = {}
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                temp = num[i] + num[j]
                if temp in twoSum:
                    twoSum[temp].append((i,j))
                else:
                    twoSum[temp] = [(i,j)]
                    
        
        res = set()      
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                newTarget = target - (num[i] + num[j])
                if newTarget in twoSum:
                    for pair in twoSum[newTarget]:
                        (p, q) = pair
                        if (i!= p) and (i != q) and (j!= p) and (j != q):
                            OneSolution = [num[i],num[j],num[p],num[q]]
                            OneSolution.sort()
                            OneSolution = tuple(OneSolution)
                            res.add(OneSolution)
                            
        return [list(i) for i in res]
        
