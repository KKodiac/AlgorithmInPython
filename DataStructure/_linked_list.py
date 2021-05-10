"""
    ADT for Linked List in Python
    prepend(value) : Add a node in the beginning
    append(value)  : Add a node in the end
    pop()          : Remove a node from the end
    popFirst()     : Remove a node from the beginning

    head()         : Return the first node
    tail()         : Return the last node
    remove(Node)   : Remove Node from the list
"""

class Node:
    def __init__(self, value : int, next_node=None):
        self.value = value
        if(next_node):
            self.next_node = next_node
        else:
            self.next_node = None
        
    def __str__(self):
        return f'Node(Value : {self.value}, Next : {self.next_node})'
class LinkedList:
    """
            Linked List (Singly Linked)
        Implemented with tail referencing the end node
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value : int):
        new_node = Node(value)
        if(self.is_empty()):
            self.head = new_node
        else:
            last_node = self.tail
            last_node.next_node = new_node
            
        self.tail = new_node
    
    def preppend(self, value : int):
        new_node = Node(value, next_node=self.head)
        self.head = new_node

    def pop(self):
        current_node = self.head
        previous_node = None

        while(current_node):
            if(current_node.next_node):
                previous_node = current_node
            else:
                return current_node
            previous_node = current_node
            current_node = current_node.next_node
            
    def popFirst(self):
        current_node = self.head
        self.head = self.head.next_node

        return current_node

    def remove(self, value):
        current_node = self.head
        previous_node = None

        while(current_node):
            if(current_node.value == value):
                previous_node.next_node = current_node.next_node
                return current_node
            
            
            previous_node = current_node
            current_node = current_node.next_node
    
    def __str__(self):
        values = []

        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node
        return ",".join(map(str, values))
    
    def is_empty(self):
        return self.head is None


def main():
    ll = LinkedList()
    ll.append(10)
    ll.append(11)
    ll.preppend(9)
    print("printint linked list", ll)
    print("popping element: ", ll.pop())
    print("popping first element : ", ll.popFirst())
    print("printing linked list", ll)
if __name__ == '__main__':
    main()
