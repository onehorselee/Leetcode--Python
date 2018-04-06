# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toInteger(node):
            if node:
                return node.val + toInteger(node.next) * 10
            else:
                return 0
                       
        n = toInteger(l1) + toInteger(l2)
        
        head = tail = ListNode(n%10)
        
        while n > 9:
            n = int(n/10)
            tail.next = ListNode(n%10)
            tail = tail.next
            
        return head
        
