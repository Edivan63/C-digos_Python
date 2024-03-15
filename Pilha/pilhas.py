class pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_str):
    stack = pilha()
    for char in input_str:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Testes
strings = ["Seja Bem Vindo!", "12345", "Python is awesome", "Testing 123..."]
for string in strings:
    print("Original:", string)
    print("Reversa:", reverse_string(string))
    print()
