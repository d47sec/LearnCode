class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

def insertNode(root, value):
    if root is None:
        return TreeNode(value) 
    else:
        if root.val == value:
            return root
        elif root.val < value:
            root.right = insertNode(root.right, value)
        else:
            root.left = insertNode(root.left, value)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
        

def searchTree(root, target): # binary search use recursion 
    
    # if root is None:
    #     return 'EO THAY'
    # if root.val == target:
    #     return 'IAMHERE'
    
    if root is None or root.val == target:
        return root
    elif root.val < target:
        return searchTree(root.right, target)
    else:
        return searchTree(root.left, target)
    

def create(seq):
    root = None
    for word in seq:
        root = insertNode(root, word)
    return root
        
 
# Print inoder traversal of the BST
tree = create([4,2,3,6,7,9,1])
# nếu là một cái mảng đã được sắp xếp thì độ phức tạp của việc sử dụng binary search tree là trường hợp xấu nhất 0(N)
# cách này chỉ sử dụng khi mảng là chưa được sắp xếp 
inorder(tree)
print(searchTree(tree, 9))
