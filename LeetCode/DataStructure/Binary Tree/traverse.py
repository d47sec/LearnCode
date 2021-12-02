# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def preorderTraversal(root) -> list[int]:
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inorderTraversal(root) -> list[int]:
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preorderTraversal(root)
print("="*20)
inorderTraversal(root)
        
        