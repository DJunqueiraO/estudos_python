class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTreeNode | None = None
        self.right: BinaryTreeNode | None = None

    def __str__(self):
        value = self.value if self.value is not None else 'null'
        left = self.left if self.left is not None else 'null'
        right = self.right if self.right is not None else 'null'
        return f'{{"value": {value}, "left": {left}, "right": {right}}}'

    def get_next_direction(self, value):
        return 'left' if value < self.value else 'right'

    def get_next(self, value):
        return getattr(self, self.get_next_direction(value))

    def set_next(self, value):
        setattr(self, self.get_next_direction(value), BinaryTreeNode(value))


class BinaryTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None

    def _appending(self, node, value):
        if not node.get_next(value):
            node.set_next(value)
        else:
            self._appending(node.get_next(value), value)

    def append(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
        else:
            self._appending(self.root, value)

    def _deleting(self, node: BinaryTreeNode, value):
        if not node:
            return None

        direction = node.get_next_direction(value)
        if value == node.value:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = self._deleting(node.right, successor.value)
        else:
            setattr(node, direction, self._deleting(node.get_next(value), value))

        return node

    def delete(self, value):
        if self.root:
            self.root = self._deleting(self.root, value)

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.get_next(value)
        return False

    def __str__(self):
        return str(self.root)


binary_tree = BinaryTree()

binary_tree.append(8)
binary_tree.append(4)
binary_tree.append(12)
binary_tree.append(2)
binary_tree.append(6)
binary_tree.append(10)
binary_tree.append(14)
binary_tree.append(1)
binary_tree.append(3)
binary_tree.append(5)
binary_tree.append(7)
binary_tree.append(9)
binary_tree.append(11)
binary_tree.append(13)
binary_tree.append(15)

binary_tree.delete(15)


# print(binary_tree.search(22))
# print(binary_tree.search(12))

print(binary_tree)
