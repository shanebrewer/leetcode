# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        maxLength = 0
        result = []
        
        if len(l1) > len(l2):
            maxLength = len(l2)
        else if len(l2) < len(l1):
            maxLength = len(l1)
        else:
            maxLength = 
            
        
        carry = 0
            
        while l1 != None or l2 != None:
            digitSum = l1 + l2 + carry
            if digitSum > 9:
                carry = 1
                result[i] = ListNode(digitSum % 10)
            else:
                result[i] = ListNode(digitSum)
        
        
        return result                
