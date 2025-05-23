class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(root: BinaryTree) -> int:
    max_diameter = 0

    def dno(node):
        nonlocal max_diameter
        if not node:
            return 0
        left_dno = dno(node.left)
        right_dno = dno(node.right)
        max_diameter = max(max_diameter, left_dno + right_dno)
        return max(left_dno, right_dno) + 1

    dno(root)
    return max_diameter




root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)

print(binary_tree_diameter(root))  


