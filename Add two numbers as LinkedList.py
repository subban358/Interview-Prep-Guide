class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode(0)
        newHead = new
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            current_sum = l1_val + l2_val + carry
            carry = current_sum // 10
            last_digit = current_sum % 10
            newNode = ListNode(last_digit)
            newHead.next = newNode
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            newHead = newHead.next
        if carry > 0:
            newNode = ListNode(carry)
            newHead.next = newNode
            newHead = newHead.next
        return new.next
            
