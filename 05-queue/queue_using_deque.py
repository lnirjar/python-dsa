from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def front(self):
        if not self.is_empty():
            return self.buffer[-1]
    
    def __len__(self):
        return len(self.buffer)
    
    def __str__(self):
        return f'Queue {self.buffer}'
    
if __name__ == '__main__':
    queue = Queue()
    print(queue, f'({len(queue)})')
    queue.enqueue('A')
    print(queue, f'({len(queue)})')
    queue.enqueue('B')
    print(queue, f'({len(queue)})')
    queue.enqueue('C')
    print(queue, f'({len(queue)})')
    print(queue.is_empty())
    print(queue.front())
    print(queue.dequeue())
    print(queue, f'({len(queue)})')
    print(queue.front())
    print(queue.dequeue())
    print(queue, f'({len(queue)})')
    print(queue.front())
    print(queue.dequeue())
    print(queue, f'({len(queue)})')
    print(queue.is_empty())
    print(queue.front())
