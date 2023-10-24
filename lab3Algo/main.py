class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    def check_balanced_and_height(node):
        if node is None:
            return True, 0

        left_balanced, left_height = check_balanced_and_height(node.left)
        right_balanced, right_height = check_balanced_and_height(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) +1
        return balanced, height

    balanced, _ = check_balanced_and_height(node)
    return balanced

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(5)
root.left.left.right = BinaryTree(7)
root.left.right = BinaryTree(5)

print(is_tree_balanced(root))