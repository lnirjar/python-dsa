class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current_node = self.head
        list_string = 'HEAD --> '
        while current_node:
            list_string += str(current_node.data) + ' --> '
            current_node = current_node.next
        list_string += 'None ' + f'({self.get_length()})'
        print(list_string)

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print('Invalid index')
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            if index == count:
                node = Node(data, current_node.next)
                current_node.next = node
                return
            current_node = current_node.next



    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print('Invalid index')
            return
        
        if index == 0:
            temp = self.head
            self.head = temp.next
            return temp.data
        
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            if count == index:
                temp = current_node.next
                current_node.next = temp.next
                return temp.data
            current_node = current_node.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.insert_at_end('E')
    ll.print()
    ll.insert_at_begining('A')
    ll.print()
    ll.insert_at_begining('B')
    ll.print()
    ll.insert_at_end('C')
    ll.print()
    ll.insert_at_end('D')
    ll.print()
    ll.insert_at(0, 'F')
    ll.print()
    ll.insert_at(6, 'G')
    ll.print()
    ll.insert_at(1, 'H')
    ll.print()
    ll.insert_at(3, 'I')
    ll.print()
    ll.remove_at(8)
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.insert_values(['A', 'B', 'C'])
    ll.print()
