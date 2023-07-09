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
    
    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                node = Node(data_to_insert, current_node.next)
                current_node.next = node
                return
            current_node = current_node.next
        print('value not found')

    def remove_by_value(self, data):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data != data:
                prev_node = current_node
                current_node = current_node.next
                continue
            if prev_node is None:
                self.remove_at(0)
                return
            prev_node.next = current_node.next
            return
        print('value not found')

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
