class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        import statistics as stats
        
        if not A and B:
            return stats.median(B)
        if not B and A:
            return stats.median(A)
        if not A and not B:
            return 0
        
        k = len(A) + len(B)
        
        if k % 2 != 0:                   # we need to find the (k-1)/2
            med_index = int((k - 1)/2) 
            odd_case = True
        else:                        
            med_index = int(k/2)          # we need to find k/2 and k/2 - 1
            odd_case = False
            
            
        k -= 1
        m = len(A) -1
        n = len(B) -1
        A = A + [0 for i in range(len(B))]

        
        
        while m >= 0 and n >= 0 and k >= med_index - 1:
            if A[m] > B[n]:
                A[k] = A[m]
                k -=1
                m -=1
            else:
                A[k] = B[n]
                k -=1
                n -=1

        while (n >= 0 and k >= med_index - 1):
            A[k] = B[n]
            k -=1
            n -=1
                
        if odd_case:
            return A[med_index]
        else:
            return (A[med_index] + A[med_index -1])/2
                
                
            
        
        
