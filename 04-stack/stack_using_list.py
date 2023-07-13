# The issue with using a list as a stack is that list uses dymanic array internally 
# and when it reaches its capacity it will reallocate a big chunk of memory 
# somewhere else in memory area and copy all the elements.
# So overhead here is: 
#   (1) allocate new memory plus 
#   (2) copy all existing elements in new memory area

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        return self.arr.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
        
    def is_empty(self):
        return len(self.arr) == 0
    
    def size(self):
        return len(self.arr)
    
    def __str__(self):
        return f'stack {self.arr}'
    
    def __len__(self):
        return len(self.arr)

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
