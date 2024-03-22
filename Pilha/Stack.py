class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ""
    while stack.top is not None:
        reversed_string += stack.pop()

    return reversed_string

# Testes
strings = [
    "Hello, world!",
    "12345",
    "Python is awesome",
    "racecar",
    "Testing with spaces and special characters: !@#$%^&*()",
]

for string in strings:
    print(f"Original: {string}")
    print(f"Reversed: {reverse_string(string)}")
    print()