"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        copyMap = {}
        current = head
        while current:
            newNode = Node(current.val)
            copyMap[current] = newNode
            current = current.next
            
        current = head
        while current:
            if current.next == None:
                copyMap[current].next = None
            else:    
                copyMap[current].next = copyMap[current.next]
            if current.random == None:
                copyMap[current].random = None
            else:
                copyMap[current].random = copyMap[current.random]            
            current = current.next
            
        return copyMap[head]    
        
            
        

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        current = head
        while current:
            newNode = Node(current.val)
            newNode.next = current.next
            current.next = newNode
            current = current.next.next
            
        current = head
        while current:
            temp = current.random
            if temp:
                current.next.random = current.random.next
            else:
                current.next.random = None
            current = current.next.next
        clone = head.next
        current = head
        while current.next:
            temp = current.next
            current.next = current.next.next
            current = temp
        return clone
            
    
