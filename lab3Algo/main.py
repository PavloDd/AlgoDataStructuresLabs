from collections import deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    # def check_balanced(node):
    #     if node is None:
    #         return True, 0
    #
    #     l_balanced, l_height = check_balanced(node.left)
    #     r_balanced, r_height = check_balanced(node.right)
    #
    #     balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
    #     height = max(l_height, r_height) + 1
    #     return balanced, height
    #
    # balanced, _ = check_balanced(node)
    # return balanced
    stack = deque([(node, 1)])
    while stack:
        current_node, height = stack.pop()
        if current_node.right:
            stack.append((current_node.right, height + 1))
        if current_node.left:
            stack.append((current_node.left, height + 1))
        if not current_node.left and not current_node.right:
            min_height = float('inf')
            max_height = float('-inf')
            for _, height in stack:
                min_height = min(min_height, height)
                max_height = max(max_height, height)
            if max_height - min_height > 1:
                return False
    return True


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(5)
root.left.left.right = BinaryTree(7)
root.left.right = BinaryTree(5)

print(is_tree_balanced(root))