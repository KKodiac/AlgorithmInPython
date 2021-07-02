class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def display(self):
        print(self.data)

    
    def insert(self, data):
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

        else:
            self.data = data

            