class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forward(self):
        list_string = 'HEAD <--> '
        current_node = self.head
        while current_node:
            list_string += f'{current_node.data} <--> '
            current_node = current_node.next
        list_string += f'TAIL ({self.get_length()})'
        print(list_string)

    def print_backward(self):
        list_string = 'TAIL <--> '
        current_node = self.tail
        while current_node:
            list_string += f'{current_node.data} <--> '
            current_node = current_node.prev
        list_string += f'HEAD ({self.get_length()})'
        print(list_string)

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return
        temp = self.head
        node = Node(data, temp, None)
        self.head = node
        temp.prev = node
        return
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return
        temp = self.tail
        node = Node(data, None, temp)
        self.tail = node
        temp.next = node
        return
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print('Invalid index')
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        if index == self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            if index == count:
                next_node = current_node.next
                node = Node(data, next_node, current_node)
                current_node.next = node
                next_node.prev = node
                return
            current_node = current_node.next
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print('Invalid index')
            return
        
        if index == 0:
            node = self.head
            next_node = node.next
            self.head = next_node
            next_node.prev = None
            return node.data
        
        if index == self.get_length() - 1:
            node = self.tail
            prev_node = node.prev
            self.tail = prev_node
            prev_node.next = None
            return node.data
        
        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                return current_node.data
            current_index += 1
            current_node = current_node.next
    
    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_begining('A')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_begining('B')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_begining('C')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_end('D')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_end('E')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_end('F')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(0, 'G')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(7, 'H')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(3, 'I')
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(8)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(3)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(0)
    dll.print_forward()
    dll.print_backward()
    dll.insert_values(['X', 'Y', 'Z'])
    dll.print_forward()
    dll.print_backward()