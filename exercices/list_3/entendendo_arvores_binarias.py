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

class BinaryTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None

    def _appending(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = BinaryTreeNode(value)
            else:
                self._appending(node.left, value)
        else:
            if not node.right:
                node.right = BinaryTreeNode(value)
            else:
                self._appending(node.right, value)

    def append(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
        else:
            self._appending(self.root, value)

    def _deleting(self, node: BinaryTreeNode, value):
        if value < node.value:
            node.left = self._deleting(node.left, value)
        elif value > node.value:
            node.right = self._deleting(node.right, value)
        else:
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

        return node

    def delete(self, value):
        if not self.root:
            return
        else:
            self.root = self._deleting(self.root, value)

    def search(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def __str__(self):
        if not self.root:
            return "Árvore vazia"
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


# print(binary_tree.search(22))
# print(binary_tree.search(12))

print(binary_tree)
