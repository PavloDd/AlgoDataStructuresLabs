class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    def check_balanced(node):
        if node is None:
            return True, 0

        l_balanced, l_height = check_balanced(node.left)
        r_balanced, r_height = check_balanced(node.right)

        balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
        height = max(l_height, r_height) + 1
        return balanced, height

    balanced, _ = check_balanced(node)
    return balanced

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(5)
root.left.left.right = BinaryTree(7)
root.left.right = BinaryTree(5)

print(is_tree_balanced(root))