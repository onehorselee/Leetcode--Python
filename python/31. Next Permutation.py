class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        
        # search the largest index that  satisfy: nums[i] < nums[i+1]               
        right = len(nums)-2
        while nums[right] >=nums[right + 1] and right >= 0:
            right -= 1

        first_small = right        
            
        # check the exception case
        if first_small == -1:
            nums[:] = nums[:][::-1]
            return 
            
        # if not the exception case, search the first number that's larger than the first-small
        first_large = -1        
        for j in range(len(nums)-1, first_small, -1):                    
            if nums[j] > nums[first_small]:
                first_large = j
                break
                
        # swap
        nums[first_small], nums[first_large] = nums[first_large], nums[first_small]
        
        # sort
        nums[first_small + 1:] = sorted(nums[first_small + 1:])
        return
            
        

        
