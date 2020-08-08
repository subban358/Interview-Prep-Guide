def isSumProperty(root):
    if root == None: 
        return 1
    if root.left == None and root.right == None:
        return 1
    Sum = 0    
    if root.left:
        Sum += root.left.data
    if root.right:
        Sum += root.right.data
    ans = root.data == Sum and isSumProperty(root.left) and isSumProperty(root.right)
    if ans: return 1
    return 0
