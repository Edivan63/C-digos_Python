class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, data):
        """
        Insere um novo nó com o valor 'data' no final da lista encadeada.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def exibir_lista(self):
        """
        Exibe os elementos da lista encadeada.
        """
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def remover_duplicados(self):
        """
        Remove os elementos duplicados da lista encadeada.
        """
        if self.head is None:
            return

        seen = set()
        current = self.head
        previous = None

        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

# Exemplo de uso:
if __name__ == "__main__":
    lista = LinkedList()
    lista.inserir(100)
    lista.inserir(220)
    lista.inserir(320)
    lista.inserir(220)
    lista.inserir(405)
    lista.inserir(320)
    lista.inserir(56)

    print("Lista encadeada original:")
    lista.exibir_lista()

    lista.remover_duplicados()

    print("Lista encadeada após remover duplicatas:")
    lista.exibir_lista()
