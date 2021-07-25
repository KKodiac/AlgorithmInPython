class DList:
    class Node:
        def __init__(self,item,prev,link):
            self.item = item
            self.prev = prev
            self.next = link
 
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.cur = self.tail
 
    def insert(self,p,item):
        t = p.prev
        n = self.Node(item,t,p)
        p.prev = n
        t.next = n
 
    def delete(self,x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
 
    def print_list(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p = p.next
 