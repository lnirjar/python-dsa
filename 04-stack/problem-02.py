# Write a function in python that checks if paranthesis in the string 
# are balanced or not. Possible parantheses are "{}',"()" or "[]". 
# Use Stack class from the tutorial.

from stack_using_deque import Stack

def is_balanced(text):
    brackets_dict = {
        '{': '}',
        '(': ')',
        '[': ']',
        '}': '{',
        ')': '(',
        ']': '['
    }
    stack = Stack()
    for char in text:
        if char in ['{', '(', '[']:
            stack.push(char)
        if char in ['}', ')', ']']:
            if stack.is_empty() or brackets_dict[char] != stack.pop():
                return False
    return stack.is_empty()

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
