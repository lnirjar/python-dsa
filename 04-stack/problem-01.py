# Write a function in python that can reverse a string using stack data structure. 
# Use Stack class from the tutorial.

from stack_using_deque import Stack

def reverse_string(text):
    reverse_text = ''
    stack = Stack()
    for char in text:
        stack.push(char)
    
    for i in range(len(text)):
        reverse_text += stack.pop()

    return reverse_text

if __name__ == '__main__':
    print(reverse_string('We will conquere COVID-19'))
    print(reverse_string('Hello World'))
