"""
    Implementation of List in Python 3
    Abstract Data Type 
    add_last(list, item)  : Adds an element at the end
    add_first(list, item) : Adds and element at the beginning
    add(list, pos, item)  : Adds an element at index pos
    delete(list, pos)     : Removes element at index pos
    clear(list)           : Removes all elements from list
    replace(list, pos, item) : Replaces element at index pos to item
    is_in_list(list, item) : Checks whether item is in list
    get_entry(list, pos)  : Returns element at index pos
    get_length(list)      : Returns length of list
    is_empty(list)        : Returns whether list is empty
    is_full(list)         : Returns whether list is full
    display(list)         : Prints all elements in list
"""

class List:
    def __init__(self, _max : int=10):
        self._list : list = list()
        self._max  : int = _max

    def __add__(self, other) -> list:
        return self._list.__add__(other._list)

    def is_empty(self) -> bool:
        return len(self._list)
    
    def is_full(self) -> bool:
        return len(self._list) == self._max

    def add_last(self, item):
        self._list.insert(-1, item)
    
    def add_first(self, item):
        self._list.insert(0, item)

    def add(self, pos, item):
        if(not self.is_full()):
            self.insert(pos, item)
        else:
            raise ListException(self._list, f"add:{pos}")

    def delete(self, pos):
        if(pos < 0 or pos >= self._max):
            raise ListException(self._list, f"delete:{pos}")
        else:
            self._list.pop(pos)
    
    def clear(self):
        self._list = list()

    def replace(self, pos, item):
        if(self._list[pos]):
            self._list[pos] = item
        else:
            raise ListException(self._list, f"replace:{pos}")

    def is_in_list(self, item) -> bool:
        return item in self._list
    
    def get_entry(self, pos):
        if(self._list[pos]):
            return self._list[pos]
        else:
            raise ListException(self._list, f"get_entry:{pos}")

    def get_length(self):
        return len(self._list)
      
    def display(self):
        print(*self._list)

class ListException(Exception):
    def __init__(self, _l : List[any], message : str = "List Exception"):
        self._l : list = _l
        self.message = message
        super().__init__(self.message)

    def __repr__(self):
        return f'List Exception on {self._l} : {self.message}'

if __name__ == "__main__":
    _list = List()
    _list.add_last(10)
    _list.add_last(20)
    _list.add_last(30)
    _list.add_last(40)
    _list.display()
    _list.add_first(50)
    _list.display()
    _list.clear()
    