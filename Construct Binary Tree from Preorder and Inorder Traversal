# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTreeUtil(self, preorder, inorder, inStart, inEnd):
        if inStart > inEnd: return None
        current = preorder[self.preIndex]
        self.preIndex += 1
        
        root = TreeNode(current)
        
        inIndex = self.indexMap[root.val]
        root.left = self.buildTreeUtil(preorder, inorder, inStart, inIndex-1)
        root.right = self.buildTreeUtil(preorder, inorder, inIndex+1, inEnd)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preIndex = 0
        self.indexMap = {}
        for index, val in enumerate(inorder):
            self.indexMap[val] = index
        return self.buildTreeUtil(preorder, inorder, 0, len(inorder)-1)
