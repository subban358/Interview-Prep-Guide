# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeUtil(self, postorder, inorder, inStart, inEnd):
        if inStart > inEnd: 
            return None
        
        current = postorder[self.postIndex]
        self.postIndex -= 1
        
        root = TreeNode(current)
        inIndex = self.indexMap[root.val]
        
        root.right = self.buildTreeUtil(postorder, inorder, inIndex+1, inEnd)
        root.left = self.buildTreeUtil(postorder, inorder, inStart, inIndex-1)
        return root
        
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postIndex = len(postorder)-1
        self.indexMap = {}
        for index, val in enumerate(inorder):
            self.indexMap[val] = index
        return self.buildTreeUtil(postorder, inorder, 0, len(inorder)-1)
