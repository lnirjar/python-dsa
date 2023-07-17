# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

from queue_using_deque import Queue

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('1')
    for i in range(10):
        num = queue.dequeue()
        print(num)
        
        queue.enqueue(f'{num}0')
        queue.enqueue(f'{num}1')
