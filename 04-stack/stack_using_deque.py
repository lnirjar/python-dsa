from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return f'stack {self.container}'
    
    def __len__(self):
        return len(self.container)

if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push('A')
    print(stack)
    stack.push('B')
    print(stack)
    stack.push('C')
    print(stack)
    stack.push('D')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.size())
    print(len(stack))
    stack.pop()
    print(stack)
