class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

class LinkedList:
    def __init__(self):
        self.head: Node = None

    # Exercício 1: Implemente o método 'append' para adicionar um nó no final da lista.
    # Defina a função 'append' que recebe um valor e cria um novo nó com esse valor,
    # inserindo-o ao final da lista.
    def append(self, data):
        appending_node = Node(data)
        if self.head is None:
            self.head = appending_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = appending_node

    # Exercício 2: Implemente o método 'prepend' para adicionar um nó no início da lista.
    # Defina a função 'prepend' que recebe um valor e cria um novo nó com esse valor,
    # inserindo-o no início da lista.
    def prepend(self, data):
        prepending_node = Node(data)
        prepending_node.next = self.head
        self.head = prepending_node

    # Exercício 3: Implemente a função 'delete' para remover o primeiro nó com o valor fornecido.
    # A função deve percorrer a lista e, quando encontrar um nó com o valor correspondente,
    # removê-lo da lista.
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
        last_node = self.head
        while last_node.next:
            if last_node.next.data == data:
                last_node.next = last_node.next.next
                break
            last_node = last_node.next

    # Exercício 4: Implemente o método 'search' para encontrar um nó com um valor específico.
    # A função 'search' deve percorrer a lista e retornar True se o valor for encontrado,
    # ou False se o valor não estiver na lista.
    def search(self, data):
        last_node = self.head
        while last_node:
            if last_node.data == data:
                return True
            last_node = last_node.next
        return False

    # Exercício 5: Implemente o método 'print_list' para imprimir todos os elementos da lista.
    # A função 'print_list' deve percorrer a lista e imprimir o valor de cada nó,
    # de forma que os valores sejam separados por espaço.
    def print_list(self, *values, end: str = ''):
        last_node = self.head
        print(*values, end='')
        while last_node:
            print(last_node.data, end=" ")
            last_node = last_node.next
        print(end=end)

    def __str__(self):
        last_node = self.head
        value = '['
        while last_node:
            value += f'{last_node.data}'
            if last_node.next:
                value += ', '
            last_node = last_node.next
        return f'{value}]'

# Teste sua lista com os seguintes exemplos:

linked_list = LinkedList()

# 1. Adicione alguns elementos usando 'append' e 'prepend'.

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.prepend(0)
#
# linked_list.print_list('\n')

# 2. Remova um elemento usando 'delete'.

linked_list.delete(2)
#
# linked_list.print_list('\n\n', end='\n\n')

# 3. Busque por um valor usando 'search'.

# print(linked_list.search(1))
# print(linked_list.search(2))

# 4. Imprima a lista usando 'print_list'.

# linked_list.print_list('\n', end='\n')

print(linked_list)
