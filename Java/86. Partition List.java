/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
    	if(head==null) return head;
    	ListNode dummy = new ListNode(0);
    	dummy.next = head;
    	ListNode left = dummy;
    	ListNode prev = dummy;
    	ListNode curr = head;
    	while(curr!=null){
    		if(prev==left){
    			if(curr.val<x) left = left.next;
    			prev = curr;
    			curr = curr.next;
    		}else{
    			if(curr.val >= x){
    				prev = curr;
    				curr = curr.next;
    			}else{
    				prev.next = curr.next;
    				curr.next = left.next;
    				left.next = curr;
    				left = left.next;
    				curr = prev.next;
    			}
    		}
    	}
    	return dummy.next;        
    }
}