# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second=head
        first=head.next
        while first and second:
            gcd=ListNode(math.gcd(first.val,second.val))
            second.next=gcd
            gcd.next=first
            second=first
            first=first.next
        return head    