# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while list1 or list2 or carry:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            val = v1 + v2 + carry 

            carry = val // 10 
            val = val % 10

            curr.next = ListNode(val)
            list1 = list1.next if list1 else 0
            list2 = list2.next if list2 else 0
            curr = curr.next
        return dummy.next


             

