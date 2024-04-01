class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front == None:
            raise Exception("Queue is empty")
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp.value
    
    def peek(self):
        if self.front == None:
            raise Exception("Queue is empty")
        return self.front.value
    
    def is_empty(self):
        return self.front == None
    
    def display_queue(self):
        current = self.front
        while current != None:
            print(current.value, end=" ")
            current = current.next

# Teste de uso da fila
q = Queue()

# Enfileirando os elementos 10, 20, 30 e 40
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

# Exibindo a fila após enfileirar 10, 20, 30 e 40
print("Fila após enfileirar 10, 20, 30 e 40:")
q.display_queue()

# Enfileirando os elementos 4, 5 e 6
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

# Exibindo a fila após enfileirar 4, 5 e 6
print("\nFila após enfileirar 4, 5 e 6:")
q.display_queue()

# Desenfileirando dois elementos
q.dequeue()
q.dequeue()

# Exibindo a fila após desenfileirar dois elementos
print("\nFila após desenfileirar dois elementos:")
q.display_queue()

# Visualizando o primeiro elemento da fila
primeiro_elemento = q.peek()

# Imprimindo o valor do primeiro elemento
print("\nPrimeiro elemento da fila:", primeiro_elemento)

# Verificando se a fila está vazia
fila_vazia = q.is_empty()

# Imprimindo se a fila está vazia ou não
if fila_vazia:
    print("Fila está vazia")
else:
    print("Fila não está vazia")
