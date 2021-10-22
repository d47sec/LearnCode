# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # SOLUTION1 : SỬ DỤNG SET 
    def hasCycle(self, head) -> bool:
        node_set = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False
    # SOLUTION2 : ĐÁNH DẤU NHỮNG THẰNG ĐÃ ĐI QUA
    
    def hasCycle(self, head) -> bool:
        temp = head
        while temp:
            if temp.val == None:
                return True
            temp.val = None
            temp = temp.next
    
    