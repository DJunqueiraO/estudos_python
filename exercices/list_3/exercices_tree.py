class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_next_direction(self, value):
       return 'left' if value < self.value else 'right'

    def get_next(self, value):
        return getattr(self, self.get_next_direction(value))

    def set_next(self, value):
        return setattr(self, self.get_next_direction(value), BinaryTreeNode(value))

# Exercícios:
class BinaryTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None

    def _appending(self, node: BinaryTreeNode, value):
        if node.get_next(value) is None:
            node.set_next(value)
        else:
            self._appending(node.get_next(value), value)

    def append(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self._appending(self.root, value)

    # 1. Imprima os elementos da árvore em ordem crescente.
    # Dica: Utilize o método inorder_traversal().
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    # 2. Escreva uma função para encontrar o maior elemento da árvore.
    # Dica: O maior elemento está no último nó à direita.
    def get_max_value(self):
        if not self.root:
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    # 3. Escreva uma função para encontrar o menor elemento da árvore.
    # Dica: O menor elemento está no último nó à esquerda.
    def get_min_value(self):
        if not self.root:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    # 4. Implemente uma função que conte o número total de nós na árvore.
    # Dica: Utilize recursão para contar os nós.
    def _counting(self, node: BinaryTreeNode) -> int:
        if node is None:
            return 0
        return 1 + self._counting(node.left) + self._counting(node.right)

    def __len__(self):
        return self._counting(self.root)

    # 5. Implemente uma função que retorne a altura da árvore.
    # Dica: A altura é a profundidade do nó mais profundo.
    def _calculating_height(self, node: BinaryTreeNode):
        if node is None:
            return -1
        return 1 + max(self._calculating_height(node.left), self._calculating_height(node.right))

    def get_height(self):
        return self._calculating_height(self.root)

    # 6. Verifique se um determinado valor está na árvore.
    # Dica: Faça uma busca binária recursiva.
    def search(self, value):
        node = self.root
        while node:
            if node.value == value:
                return True
            node = node.get_next(value)
        return False

    def find(self, value):
        node = self.root
        while node:
            if node.value == value:
                return node
            node = node.get_next(value)
        return None

    # 7. Liste todos os nós folhas da árvore.
    # Dica: Um nó folha é aquele que não possui filhos à esquerda nem à direita.
    def _collect_leafs(self, node, leafs):
        if not node:
            return
        if not node.left and not node.right:
            leafs.append(node.value)
        else:
            self._collect_leafs(node.left, leafs)
            self._collect_leafs(node.right, leafs)

    def get_all_leafs(self):
        leafs = BinaryTree()
        self._collect_leafs(self.root, leafs)
        return leafs

    # 8. Remova um elemento da árvore e verifique o resultado.
    # Dica: Implemente a remoção de nós levando em conta os três casos possíveis.
    def _deleting(self, node, value):
        if not node:
            return None, False
        if value < node.value:
            node.left, deleted = self._deleting(node.left, value)
        elif value > node.value:
            node.right, deleted = self._deleting(node.right, value)
        else:
            if not node.left and not node.right:
                return None, True
            if not node.left:
                return node.right, True
            if not node.right:
                return node.left, True
            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right, deleted = self._deleting(node.right, successor.value)

        return node, deleted

    def delete(self, value):
        self.root, deleted = self._deleting(self.root, value)
        return deleted

    # 9. Modifique a árvore para se tornar uma árvore binária balanceada.
    # Dica: Você pode criar um método que reconstrua a árvore a partir de uma lista ordenada.
    def _build_balanced_tree(self, sorted_list, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = BinaryTreeNode(sorted_list[mid])
        node.left = self._build_balanced_tree(sorted_list, start, mid - 1)
        node.right = self._build_balanced_tree(sorted_list, mid + 1, end)
        return node

    def from_list(self, list_):
        sorted_list = sorted(list_)
        self.root = self._build_balanced_tree(sorted_list, 0, len(sorted_list) - 1)
        return self

    # 10. Escreva uma função que encontre o caminho do nó raiz até um nó específico.
    # Dica: Percorra a árvore e armazene os nós no caminho.
    def _finding_path(self, node, value, path):
        if node is None:
            return False
        path.append(node.value)
        if node.value == value:
            return True
        if self._finding_path(node.left, value, path) or self._finding_path(node.right, value, path):
            return True
        path.pop()
        return False

    def find_path(self, value):
        path = []
        if self._finding_path(self.root, value, path):
            return path
        return None

# Criando uma árvore binária para testes
binary_tree = BinaryTree()
binary_tree.append(32)
binary_tree.append(17)
binary_tree.append(51)
binary_tree.append(3)
binary_tree.append(89)
binary_tree.append(12)
binary_tree.append(20)
binary_tree.append(25)
binary_tree.append(8)
binary_tree.append(1)

print(binary_tree.find(2))

# binary_tree.inorder_traversal(binary_tree.root)
# binary_tree.inorder_traversal(binary_tree.root)
#
# print(binary_tree.get_max_value())
#
# print(binary_tree.get_min_value())
#
# print(len(binary_tree))
#
# print(binary_tree.get_height())
#
# print(binary_tree.search(3))
#
# print(binary_tree.get_all_leafs())
#
# print(binary_tree.delete(3))
#
# print(binary_tree.search(3))

# print(binary_tree.from_list([1, 2, 3, 4]).search(1))
